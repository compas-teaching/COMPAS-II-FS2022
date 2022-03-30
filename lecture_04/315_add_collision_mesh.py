import time

from compas_fab.backends import RosClient
from compas_fab.robots import CollisionMesh
from compas_fab.robots import PlanningScene

from compas.datastructures import Mesh
from compas.geometry import Box

with RosClient("localhost") as client:
    robot = client.load_robot()
    scene = PlanningScene(robot)

    box = Box.from_diagonal([(-0.7, -0.7, 0), (.7, .7, -0.02)])
    mesh = Mesh.from_shape(box)
    cm = CollisionMesh(mesh, "floor")
    scene.add_collision_mesh(cm)

    # sleep a bit before terminating the client
    time.sleep(1)
