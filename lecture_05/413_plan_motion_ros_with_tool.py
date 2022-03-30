import math
import os

from compas_fab.backends import RosClient
from compas_fab.robots import Tool
from helpers import show_trajectory

from compas.datastructures import Mesh
from compas.geometry import Frame

HERE = os.path.dirname(__file__)

# create tool from mesh and frame
mesh = Mesh.from_stl(os.path.join(HERE, "vacuum_gripper.stl"))
tool = Tool(mesh, Frame([0, 0, 0.07], [1, 0, 0], [0, 1, 0]), link_name="wrist_3_link")

with RosClient("localhost") as client:
    robot = client.load_robot()
    group = robot.main_group_name

    frame = Frame((0.4, 0.3, 0.05), (-1, 0, 0), (0, 1, 0))
    tolerance_position = 0.001
    tolerance_axes = [math.radians(1)] * 3

    start_configuration = robot.zero_configuration()
    start_configuration.joint_values = (-0.045, 5.073, 2.114, -2.475, 4.712, 1.526)

    # Attach the tool
    robot.attach_tool(tool)

    # Adjust frame based on attached tool
    frame = robot.from_tcf_to_t0cf([frame])[0]

    # create goal constraints from frame
    goal_constraints = robot.constraints_from_frame(frame, tolerance_position, tolerance_axes, group)

    trajectory = robot.plan_motion(goal_constraints, start_configuration, group, options=dict(planner_id="RRT"))

    print("Computed kinematic path with %d configurations." % len(trajectory.points))
    print("Executing this path at full speed would take approx. %.3f seconds." % trajectory.time_from_start)

    show_trajectory(trajectory)
