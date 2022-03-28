"""Assignment 03: Using inverse kinematics
"""
import os
import compas
import math
from compas_fab.backends import RosClient
from compas_fab.robots import Configuration

from compas.geometry import Frame
from compas.geometry import Point
from compas.geometry import Vector


# Step 1: Inside this function, complete the main part of the solution for the assignment:
#  - Taking a robot and a list of frames as parameter, calculate a feasible configuration for each of the frames
#  - Try to find an optimal start_configuration for each so that the motion from one config to the next is minimized
def calculate_ik_for_frames(robot, frames):

    # # Method 1 - through inverse kinematics and assign initial profiles
    # # It works but the a good inital configuration needs to be mannually figured out
    # configs = []
    # prev_config = robot.zero_configuration()
    # prev_config.joint_values = (0.22, 3.4, -0.75, -0.97, 1.82, 4.93)
    # for i, frame in enumerate(frames):
    #     new_config = robot.inverse_kinematics(frame,prev_config)
    #     configs.append(new_config)
    #     prev_config = new_config



    #Method 2 - through plan cartesian motion
    configs = []
    group = robot.main_group_name
    zero = robot.zero_configuration()
    min_num = 5
    ## does not need to manually input a start configuration
    ## zero.joint_values = (0.22, 3.4, -0.75, -0.97, 1.82, 4.93)

    global_iter_count = 0
    global_search = False

    #will iterate through different inverse_kinematics results if it does not work
    while global_search == False and global_iter_count<20:
        configs = [] ##reclean the configs
        global_search = True
        print("In Iteration:" + str(global_iter_count))
        start_configuration = robot.inverse_kinematics(frames[0],zero)
        for i, frame in enumerate(frames):
            if i < len(frames): #interestingly the plan_cartesion returns 2 at first than more later
                point_num = 1
                iter_count = 0
                while point_num < min_num and iter_count < 10:
                    trajectory = robot.plan_cartesian_motion(frames[i:i+1],
                                                            start_configuration,
                                                            group=group,
                                                            options=dict(
                                                                planner_id="RRTConnect",
                                                                max_step=0.01,
                                                                avoid_collisions=True,
                                                            ))
                    point_num = len(trajectory.points)
                    iter_count += 1
                    print("Tractory Points between Frame" + str(i) + " &Frame" + str(i+1) +" Num: " + str( point_num))

                #if the result is not good, it will set global_search as false, then it will restart the search
                if i!= 0 and point_num < min_num and iter_count == 10:
                    print("Fail to find result between Frame"+str(i)+"and Frame" + str(i+1))
                    global_search = False
                    break
                else:
                    for tp in trajectory.points:
                        config = robot.zero_configuration()
                        config.joint_values = tp.joint_values
                        #print(robot.forward_kinematics(config))
                        configs.append(config)

                    #print("check")
                    #print(frames[i].point)
                    #print(frames[i+1].point)
                    #print("check_finish")
                    start_configuration = configs.pop(-1)

        global_iter_count+=1
    configs.append(start_configuration)

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
