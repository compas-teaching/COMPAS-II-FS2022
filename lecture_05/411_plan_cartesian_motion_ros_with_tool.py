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

    frames = []
    frames.append(Frame((0.3, 0.1, 0.05), (-1, 0, 0), (0, 1, 0)))
    frames.append(Frame((0.4, 0.3, 0.05), (-1, 0, 0), (0, 1, 0)))

    start_configuration = robot.zero_configuration()
    start_configuration.joint_values = (-0.045, 5.073, 2.114, -2.475, 4.712, 1.526)

    # Attach the tool
    robot.attach_tool(tool)

    # Adjust frames based on attached tool
    frames = robot.from_tcf_to_t0cf(frames)

    # Plan as usual
    trajectory = robot.plan_cartesian_motion(frames,
                                             start_configuration,
                                             group=group,
                                             options=dict(
                                                 max_step=0.01,
                                                 avoid_collisions=True,
                                             ))

    print("Computed cartesian path with %d configurations, " % len(trajectory.points))
    print("following %d%% of requested trajectory." % (trajectory.fraction * 100))
    print("Executing this path at full speed would take approx. %.3f seconds." % trajectory.time_from_start)

    show_trajectory(trajectory)
