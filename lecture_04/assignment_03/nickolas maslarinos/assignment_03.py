"""Assignment 03: Using inverse kinematics
"""
import os
import compas
from compas_fab.backends import RosClient
from compas_fab.robots import Configuration

from compas.geometry import Frame
from compas.geometry import Point
from compas.geometry import Vector


# Step 1: Inside this function, complete the main part of the solution for the assignment:
#  - Taking a robot and a list of frames as parameter, calculate a feasible configuration for each of the frames
#  - Try to find an optimal start_configuration for each so that the motion from one config to the next is minimized
def calculate_ik_for_frames(robot, frames):
    configs = []
    start_configuration = robot.zero_configuration()
    start_configuration.joint_values = (-0.106, 5.351, 2.231, -2.869, 4.712, 1.465)

    for i in range(len(frames)):
        if i == 0:
            config = robot.inverse_kinematics(frames[i], start_configuration)
        else:
            config = robot.inverse_kinematics(frames[i], configs[i-1])
        configs.append(config)
    return configs


# Step 2: store all found configurations in a JSON file using compas.json_dump or compas.json_dumps
def store_configurations(configurations, filename):
    compas.json_dump(configurations, filename)
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
        filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assignment_03.json')
        store_configurations(configurations, filename)
        print("Stored results in {}".format(filename))