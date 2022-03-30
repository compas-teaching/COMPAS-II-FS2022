import os
import time

from compas_fab.backends import RosClient
from compas_fab.robots import Tool

from compas.datastructures import Mesh
from compas.geometry import Frame

HERE = os.path.dirname(__file__)

# create tool from mesh and frame
mesh = Mesh.from_stl(os.path.join(HERE, "vacuum_gripper.stl"))
tool = Tool(mesh, Frame([0, 0, 0.07], [1, 0, 0], [0, 1, 0]), link_name="wrist_3_link")

with RosClient("localhost") as client:
    robot = client.load_robot()

    # Attach the tool
    robot.attach_tool(tool)

    # Do something useful with the tool...
    time.sleep(1)

    # Remove the tool
    robot.detach_tool()
