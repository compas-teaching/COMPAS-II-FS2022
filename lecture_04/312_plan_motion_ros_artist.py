import math
import time

from compas_fab.backends import RosClient

from compas.artists import Artist
from compas.geometry import Frame

with RosClient("localhost") as client:
    robot = client.load_robot(load_geometry=True)
    group = robot.main_group_name

    frame = Frame((0.4, 0.3, 0.05), (-1, 0, 0), (0, 1, 0))
    tolerance_position = 0.001
    tolerance_axes = [math.radians(1)] * 3

    start_configuration = robot.zero_configuration()
    start_configuration.joint_values = (-0.106, 5.351, 2.231, -2.869, 4.712, 1.465)

    # create goal constraints from frame
    goal_constraints = robot.constraints_from_frame(frame, tolerance_position, tolerance_axes, group)

    trajectory = robot.plan_motion(goal_constraints, start_configuration, group, options=dict(planner_id="RRT"))

    print("Computed kinematic path with %d configurations." % len(trajectory.points))
    print("Executing this path at full speed would take approx. %.3f seconds." % trajectory.time_from_start)

    artist = Artist(robot.model)

    for tp in trajectory.points:
        config = robot.zero_configuration()
        config.joint_values = tp.joint_values
        artist.update(config)
        artist.draw_visual()
        artist.redraw()
        time.sleep(0.02)
