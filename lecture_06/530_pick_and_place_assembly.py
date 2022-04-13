import math
import os

from compas_fab.backends import RosClient
from compas_fab.robots import AttachedCollisionMesh
from compas_fab.robots import CollisionMesh
from compas_fab.robots import PlanningScene
from compas_fab.robots import Tool

import compas
from compas.datastructures import Assembly
from compas.datastructures import Mesh
from compas.datastructures import Part
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Polyhedron
from compas.geometry import Translation


def get_tool():
    current_folder = os.path.dirname(__file__)
    mesh = Mesh.from_stl(os.path.join(current_folder, "vacuum_gripper.stl"))
    frame = Frame([0, 0, 0.07], [1, 0, 0], [0, 1, 0])
    tool = Tool(mesh, frame, link_name="wrist_3_link")
    return tool


def get_approach_vector(part_key):
    return (0, 0, 0.05)


def get_pick_frame(part_key):
    return Frame((0.3, 0.1, 0.05), (-1, 0, 0), (0, 1, 0))


def get_place_frame(part_key):
    return Frame((0.4, 0.3, 0.05), (-1, 0, 0), (0, 1, 0))


def get_part_frame(part_key):
    return get_place_frame(part_key).transformed(Translation.from_vector((0, 0, -0.02)))


def prepare_scene(robot, part_key):
    scene = PlanningScene(robot)
    box = Box.from_diagonal([(-0.7, -0.7, 0), (0.7, 0.7, -0.02)])
    mesh = Mesh.from_shape(box)
    scene.add_collision_mesh(CollisionMesh(mesh, "floor"))


def get_start_configuration(robot):
    config = robot.zero_configuration()
    config.joint_values = (-0.306, 4.351, 2.231, -2.869, 4.712, 1.465)
    return config


def get_part_shape(part_key):
    box = Box.from_diagonal([(-0.02, -0.05, 0), (0.02, 0.05, -0.02)])
    return Polyhedron(*box.to_vertices_and_faces(triangulated=True))


def get_number_of_parts():
    return 2


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

assembly = Assembly('picknplace')
assembly.attributes['start_configuration'] = start_configuration.data
assembly.attributes['tool'] = tool.data

for i in range(get_number_of_parts()):
    part_key = str(i)
    part = Part(part_key, shape=get_part_shape(part_key), frame=get_part_frame(part_key))
    prepare_scene(robot, part_key)

    print("Part {}\n--------".format(part_key))
    print(" [  ] Pick frame + approach vector reachability\r", flush=True, end='')
    pick_frame = adjust_to_attached_tool(robot, get_pick_frame(part_key))
    approach_pick_frame = pick_frame.transformed(
        Translation.from_vector(get_approach_vector(part_key))
    )

    approach_pick_config = robot.inverse_kinematics(
        approach_pick_frame, start_configuration
    )
    part.attributes["approach_pick_config"] = approach_pick_config
    print(" [OK]")

    print(" [  ] Pick frame\r", flush=True, end='')
    pick_config = robot.inverse_kinematics(pick_frame, approach_pick_config)
    part.attributes["pick_config"] = pick_config
    print(" [OK]")

    print(" [  ] Place frame + approach vector\r", flush=True, end='')
    place_frame = adjust_to_attached_tool(robot, get_place_frame(part_key))
    approach_place_frame = place_frame.transformed(
        Translation.from_vector(get_approach_vector(part_key))
    )

    # we use the approach pick config as start, because we estimate is the closest
    approach_place_config = robot.inverse_kinematics(
        approach_place_frame, approach_pick_config
    )
    part.attributes["approach_place_config"] = approach_place_config
    print(" [OK]")

    print(" [  ] Place frame\r", flush=True, end='')
    place_config = robot.inverse_kinematics(place_frame, approach_place_config)
    part.attributes["place_config"] = place_config
    print(" [OK]")

    print(" [  ] Pick path (before)\r", flush=True, end='')
    frames = [approach_pick_frame, pick_frame]
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

    print(" [OK]")
    part.attributes["pick_trajectory"] = pick_trajectory

    print(" [  ] Pick path (after)\r", flush=True, end='')
    frames = [pick_frame, approach_pick_frame]

    # Create ACM with shape
    part_shape = get_part_shape(part_key)
    part_mesh = Mesh.from_shape(part_shape)

    ee_link_name = robot.attached_tool.link_name
    attach_frame = robot.attached_tool.frame.copy()
    attach_frame.xaxis.x *= -1
    part_acms = [AttachedCollisionMesh(CollisionMesh(part_mesh, 'brick', attach_frame), ee_link_name)]

    pick_trajectory_after = robot.plan_cartesian_motion(
        frames,
        pick_trajectory.points[-1],
        options=dict(
            max_step=0.01,
            avoid_collisions=True,
            attached_collision_meshes=part_acms,
        ),
    )

    if pick_trajectory_after.fraction < 1.0:
        raise Exception("Found a pick trajectory (after) but it is not complete")

    print(" [OK]")
    part.attributes["pick_trajectory_after"] = pick_trajectory_after

    print(" [  ] Place path (before)\r", flush=True, end='')
    frames = [approach_place_frame, place_frame]
    place_trajectory = robot.plan_cartesian_motion(
        frames,
        approach_place_config,
        options=dict(
            max_step=0.01,
            avoid_collisions=True,
            attached_collision_meshes=part_acms,
        ),
    )

    if pick_trajectory.fraction < 1.0:
        raise Exception("Found a place trajectory but it is not complete")

    print(" [OK]")
    part.attributes["place_trajectory"] = place_trajectory

    print(" [  ] Place path (after)\r", flush=True, end='')
    frames = [place_frame, approach_place_frame]
    place_trajectory_after = robot.plan_cartesian_motion(
        frames,
        place_trajectory.points[-1],
        options=dict(
            max_step=0.01,
            avoid_collisions=True,
        ),
    )

    if place_trajectory_after.fraction < 1.0:
        raise Exception("Found a place trajectory (after) but it is not complete")

    print(" [OK]")
    part.attributes["place_trajectory_after"] = place_trajectory_after

    print(" [  ] Free space path\r", flush=True, end='')
    goal_constraints = robot.constraints_from_configuration(
        approach_place_config,
        tolerances_above=get_tolerance_joints(),
        tolerances_below=get_tolerance_joints(),
    )

    freespace_trajectory = robot.plan_motion(
        goal_constraints,
        approach_pick_config,
        options=dict(
            planner_id=get_planner_id(),
            attached_collision_meshes=part_acms,
        ),
    )
    print(" [OK]")
    part.attributes["freespace_trajectory"] = freespace_trajectory

    print(" [  ] Start config path\r", flush=True, end='')
    goal_constraints = robot.constraints_from_configuration(
        approach_pick_config,
        tolerances_above=get_tolerance_joints(),
        tolerances_below=get_tolerance_joints(),
    )

    start_trajectory = robot.plan_motion(
        goal_constraints, start_configuration, options=dict(planner_id=get_planner_id())
    )
    print(" [OK]")
    part.attributes["start_trajectory"] = start_trajectory
    print()

    assembly.add_part(part, key=part_key)


client.close()

compas.json_dump(
    assembly,
    os.path.join(os.path.dirname(__file__), "530_pick_and_place_assembly.json"),
    pretty=True,
)
