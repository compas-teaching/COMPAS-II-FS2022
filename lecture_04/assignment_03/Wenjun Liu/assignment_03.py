"""Assignment 03: Using inverse kinematics
"""
import os
import compas
from compas_fab.backends import RosClient
from compas_fab.robots import Configuration

from compas.geometry import Frame
from compas.geometry import Point
from compas.geometry import Vector

import math

# Step 1: Inside this function, complete the main part of the solution for the assignment:
#  - Taking a robot and a list of frames as parameter, calculate a feasible configuration for each of the frames
#  - Try to find an optimal start_configuration for each so that the motion from one config to the next is minimized
def calculate_ik_for_frames(robot, frames):
    # 1. Used inverse_kinematics with set start_configuration, but found it still jumping randomly from frames
    """
    configs = []
    start_config = robot.zero_configuration()
    start_config.joint_values =(-6.058, 4.186, -2.128, 5.796, -4.712, 1.796)
    for frame in frames:
        config = robot.inverse_kinematics(frame, start_config)
        configs.append(config)
        start_config = config
    return configs
    """

    # 2. Searching for better control to minimze the motion through motion plan
    configs = []
    group = robot.main_group_name
    tolerance_position = 0.001
    tolerance_axes = [math.radians(1)] * 3
    start_configuration = robot.zero_configuration()
    start_configuration.joint_values = (-6.058, 4.186, -2.128, 5.796, -4.712, 1.796)

    for frame in frames:
        goal_constraints = robot.constraints_from_frame(frame, tolerance_position, tolerance_axes, group)
        config_check = []
        motion_steps = []

        # collect possible motion paths
        for i in range(100): # Unstable results for 20 or 50, 100 should be satisfactory
            trajectory = robot.plan_motion(goal_constraints, start_configuration, group, options=dict(planner_id="RRT"))
            motion_step = len(trajectory.points)
            motion_steps.append(motion_step)
            config = robot.zero_configuration()
            config.joint_values = trajectory.points[-1].joint_values
            config_check.append(config)

        # pick path with minimun motion
        minimun_step_id = motion_steps.index(min(motion_steps))
        print(min(motion_steps))
        config = config_check[minimun_step_id]
        start_configuration = config
        configs.append(config)

    return configs

# Step 2: store all found configurations in a JSON file using compas.json_dump or compas.json_dumps
def store_configurations(configurations, filename):
    compas.json_dump(configurations,filename)
    pass

# Use the following to test from the command line
# Or copy solution_viewer.ghx next to the folder where you created assignment_03.py to visualize the same in Grasshopper
if __name__ == '__main__':

    frames = [
        Frame(Point(-0.329, 0.059, 0.082), Vector(1.000, 0.000, 0.000), Vector(0.000, -1.000, 0.000)),
        Frame(Point(-0.260, 0.129, 0.082), Vector(1.000, 0.000, 0.000), Vector(0.000, -1.000, 0.000)),
        Frame(Point(-0.186, 0.194, 0.082), Vector(1.000, 0.000, 0.000), Vector(0.000, -1.000, 0.000)),
        Frame(Point(-0.106, 0.252, 0.082), Vector(1.000, 0.000, 0.000), Vector(0.000, -1.000, 0.000)),
        Frame(Point(-0.020, 0.299, 0.082), Vector(1.000, 0.000, 0.000), Vector(0.000, -1.000, 0.000)),
        Frame(Point(0.074, 0.329, 0.082), Vector(1.000, 0.000, 0.000), Vector(0.000, -1.000, 0.000)),
        Frame(Point(0.172, 0.330, 0.082), Vector(1.000, 0.000, 0.000), Vector(0.000, -1.000, 0.000)),
        Frame(Point(0.263, 0.295, 0.082), Vector(1.000, 0.000, 0.000), Vector(0.000, -1.000, 0.000)),
        Frame(Point(0.339, 0.233, 0.082), Vector(1.000, 0.000, 0.000), Vector(0.000, -1.000, 0.000)),
        Frame(Point(0.400, 0.155, 0.082), Vector(1.000, 0.000, 0.000), Vector(0.000, -1.000, 0.000)),
        Frame(Point(0.448, 0.070, 0.082), Vector(1.000, 0.000, 0.000), Vector(0.000, -1.000, 0.000))]

    # Loads the robot from ROS
    with RosClient('localhost') as client:
        robot = client.load_robot()

        # Step 1: calculate IK solutions for each frame
        configurations = calculate_ik_for_frames(robot, frames)
        print("Found {} configurations".format(len(configurations)))

        # Step 2: store all configurations in a JSON file
        filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assignment-03.json')
        store_configurations(configurations, filename)
        print("Stored results in {}".format(filename))
