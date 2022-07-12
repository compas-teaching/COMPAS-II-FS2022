"""Assignment 03: Using inverse kinematics
"""
import os
import compas
from compas_fab.backends import RosClient
from compas_fab.robots import Configuration

from compas.geometry import Frame
from compas.geometry import Point
from compas.geometry import Vector

compas.DATA = "/Users/Maxence/opt/anaconda3/envs/fs2022/lib/python3.8/site-packages/compas/data/samples/"


def calculate_ik_for_frames(robot, frames):

    configs = []
    configs.append(robot.zero_configuration())

    for f in frames:
        start_configuration = configs[-1]
        configs.append(robot.inverse_kinematics(f, start_configuration))
    configs.pop(0)
    return configs


def store_configurations(configurations, filename):
    compas.json_dump(configurations, filename)
    # Is it supposed to be more sophiticated? I don't understand the reason to define such function.
    # Also, I don't find the difference between compas.json_dump and compas.json_dumps
    pass


# the solution_viewer.ghx can't find the assignment_03.py (which is in the same folder).
# I fixed this by loading the json into GHPython but I would like to understand why it doesn't work by default.
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

    with RosClient('localhost') as client:
        robot = client.load_robot()

        configurations = calculate_ik_for_frames(robot, frames)
        print("Found {} configurations".format(len(configurations)))
        for i in range(0, len(configurations)):
            print(configurations[i])

        filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assignment-03.json')
        store_configurations(configurations, filename)
        print("Stored results in {}".format(filename))
