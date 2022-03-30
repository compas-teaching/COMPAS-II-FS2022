import math
from compas_fab.backends import RosClient
from compas.geometry import Frame

with RosClient("localhost") as client:
    robot = client.load_robot()

    frame = Frame((0.4, 0.3, 0.05), (-1, 0, 0), (0, 1, 0))
    tolerance_position = 0.001
    tolerance_axes = [math.radians(1)] * 3

    config = robot.zero_configuration()
    config.joint_values = (-0.106, 5.351, 2.231, -2.869, 4.712, 1.465)
    tolerances_above = [0.1] * 6
    tolerances_below = [0.1] * 6

    # create goal constraints from frame
    goal_constraints = robot.constraints_from_frame(
        frame, tolerance_position, tolerance_axes
    )
    print(goal_constraints)

    # create goal constraints from frame
    goal_constraints = robot.constraints_from_configuration(
        config, tolerances_above, tolerances_below
    )
    print(goal_constraints)
