import time

from compas_fab.backends import RosClient
from compas_fab.robots import CollisionMesh
from compas_fab.robots import PlanningScene

from compas.datastructures import Mesh
from compas.geometry import Box

with RosClient("localhost") as client:
    robot = client.load_robot()
    scene = PlanningScene(robot)

    brick = Box.from_diagonal([(-0.006, -0.015, 0), (.006, .015, 0.012)])

    for i in range(5):
        mesh = Mesh.from_shape(brick)
        cm = CollisionMesh(mesh, "brick_wall")
        cm.frame.point.y = 0.5
        cm.frame.point.z = brick.zsize * i

        scene.append_collision_mesh(cm)

    # sleep a bit before terminating the client
    time.sleep(1)
