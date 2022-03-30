from compas_fab.backends import RosClient
from helpers import show_trajectory

from compas.geometry import Frame

with RosClient("localhost") as client:
    robot = client.load_robot()
    group = robot.main_group_name

    frames = []
    frames.append(Frame((0.3, 0.1, 0.05), (-1, 0, 0), (0, 1, 0)))
    frames.append(Frame((0.4, 0.3, 0.05), (-1, 0, 0), (0, 1, 0)))

    start_configuration = robot.zero_configuration()
    start_configuration.joint_values = (-0.106, 5.351, 2.231, -2.869, 4.712, 1.465)

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
