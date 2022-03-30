import math
import os

import compas
from compas_fab.backends import RosClient
from compas_fab.robots import CollisionMesh
from compas_fab.robots import PlanningScene
from compas_fab.robots import Tool

from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Translation


def get_tool():
    current_folder = os.path.dirname(__file__)
    mesh = Mesh.from_stl(os.path.join(current_folder, "vacuum_gripper.stl"))
    frame = Frame([0, 0, 0.07], [1, 0, 0], [0, 1, 0])
    tool = Tool(mesh, frame, link_name="wrist_3_link")
    return tool


def get_approach_vector(n):
    return (0, 0, 0.05)


def get_pick_frame(n):
    return Frame((0.3, 0.1, 0.05), (-1, 0, 0), (0, 1, 0))


def get_place_frame(n):
    return Frame((0.4, 0.3, 0.05), (-1, 0, 0), (0, 1, 0))


def prepare_scene(robot, n):
    scene = PlanningScene(robot)
    box = Box.from_diagonal([(-0.7, -0.7, 0), (0.7, 0.7, -0.02)])
    mesh = Mesh.from_shape(box)
    scene.add_collision_mesh(CollisionMesh(mesh, "floor"))


def get_start_configuration(robot):
    config = robot.zero_configuration()
    config.joint_values = (-0.306, 4.351, 2.231, -2.869, 4.712, 1.465)
    return config


def get_number_of_parts():
    return 1


def get_tolerance_joints():
    return [math.radians(1)] * 6


def get_planner_id():
    return "TRRT"


# PICK & PLACE PROCEDURE

def adjust_to_attached_tool(robot, frame):
    if not robot.attached_tool:
        return frame
    return robot.from_tcf_to_t0cf([frame])[0]


client = RosClient("localhost")
client.run()

robot = client.load_robot()

start_configuration = get_start_configuration(robot)

tool = get_tool()
if tool:
    robot.attach_tool(tool)

results = {"start_configuration": start_configuration, "parts": {}}

for i in range(get_number_of_parts()):
    part_key = str(i)
    results["parts"][part_key] = dict()
    prepare_scene(robot, i)

    print("Part {}\n--------".format(i))
    print(" - Testing pick frame + approach vector reachability...")
    pick_frame = adjust_to_attached_tool(robot, get_pick_frame(i))
    approach_pick_frame = pick_frame.transformed(
        Translation.from_vector(get_approach_vector(i))
    )

    approach_pick_config = robot.inverse_kinematics(
        approach_pick_frame, start_configuration
    )
    results["parts"][part_key]["approach_pick_config"] = approach_pick_config
    print(" - Pick frame + approach vector is reachable!")

    print(" - Testing pick frame reachability...")
    pick_config = robot.inverse_kinematics(pick_frame, approach_pick_config)
    results["parts"][part_key]["pick_config"] = pick_config
    print(" - Pick frame is reachable!")

    print(" - Testing place frame + approach vector reachability...")
    place_frame = adjust_to_attached_tool(robot, get_place_frame(i))
    approach_place_frame = place_frame.transformed(
        Translation.from_vector(get_approach_vector(i))
    )

    # we use the approach pick config as start, because we estimate is the closest
    approach_place_config = robot.inverse_kinematics(
        approach_place_frame, approach_pick_config
    )
    results["parts"][part_key]["approach_place_config"] = approach_place_config
    print(" - Place frame + approach vector is reachable!")

    print(" - Testing place frame reachability...")
    place_config = robot.inverse_kinematics(place_frame, approach_place_config)
    results["parts"][part_key]["place_config"] = place_config
    print(" - Place frame is reachable!")

    print(" - Testing pick path")
    frames = [approach_pick_frame, pick_frame, approach_pick_frame]
    pick_trajectory = robot.plan_cartesian_motion(
        frames,
        approach_pick_config,
        options=dict(
            max_step=0.01,
            avoid_collisions=True,
        ),
    )

    if pick_trajectory.fraction < 1.0:
        raise Exception("Found a pick trajectory but it is not complete")

    print(" - Pick path is feasible!")
    results["parts"][part_key]["pick_trajectory"] = pick_trajectory

    print(" - Testing place path")
    frames = [approach_place_frame, place_frame, approach_place_frame]
    place_trajectory = robot.plan_cartesian_motion(
        frames,
        approach_place_config,
        options=dict(
            max_step=0.01,
            avoid_collisions=True,
        ),
    )

    if pick_trajectory.fraction < 1.0:
        raise Exception("Found a place trajectory but it is not complete")

    print(" - Place path is feasible!")
    results["parts"][part_key]["place_trajectory"] = place_trajectory

    print(" - Testing free space path")
    goal_constraints = robot.constraints_from_configuration(
        approach_place_config,
        tolerances_above=get_tolerance_joints(),
        tolerances_below=get_tolerance_joints(),
    )

    freespace_trajectory = robot.plan_motion(
        goal_constraints,
        approach_pick_config,
        options=dict(planner_id=get_planner_id()),
    )
    print(" - Free space path is feasible!")
    results["parts"][part_key]["freespace_trajectory"] = freespace_trajectory

    print(" - Testing start config path")
    goal_constraints = robot.constraints_from_configuration(
        approach_pick_config,
        tolerances_above=get_tolerance_joints(),
        tolerances_below=get_tolerance_joints(),
    )

    start_trajectory = robot.plan_motion(
        goal_constraints, start_configuration, options=dict(planner_id=get_planner_id())
    )
    print(" - Start config path is feasible!")
    results["parts"][part_key]["start_trajectory"] = start_trajectory

    print("FULL PICK&PLACE PATH FOUND!")

client.close()

compas.json_dump(
    results,
    os.path.join(os.path.dirname(__file__), "420_pick_and_place.json"),
    pretty=True,
)
