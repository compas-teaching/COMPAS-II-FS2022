"""Assignment 02: Build your own robot model
"""
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Circle
from compas.geometry import Cylinder
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Translation
from compas.robots import Configuration
from compas.robots import Joint
from compas.robots import RobotModel
import math
import compas

compas.DATA = "/Users/Maxence/opt/anaconda3/envs/fs2022/lib/python3.8/site-packages/compas/data/samples/"

# create cylinder in yz plane
radius, length = 0.7, 5
cylinder = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), length)
cylinder.transform(Translation.from_vector([length / 2.0, 0, 0]))

# create robot model
model = RobotModel("E-robot", links=[], joints=[])

# link meshes (calling Mesh.from_shape effectively creates a copy of the shape)
mesh1 = Mesh.from_shape(cylinder)
mesh2 = Mesh.from_shape(cylinder)
mesh3 = Mesh.from_shape(cylinder)
mesh4 = Mesh.from_shape(cylinder)
mesh5 = Mesh.from_shape(cylinder)

# add links
link0 = model.add_link("world")
link1 = model.add_link("link1", visual_mesh=mesh1, visual_color=(0.2, 0.5, 0.6))
link2 = model.add_link("link2", visual_mesh=mesh2, visual_color=(0.5, 0.6, 0.2))
link3 = model.add_link("link3", visual_mesh=mesh3, visual_color=(0.7, 0.3, 0.5))
link4 = model.add_link("link4", visual_mesh=mesh4, visual_color=(0.1, 0.2, 0.8))
link5 = model.add_link("link5", visual_mesh=mesh5, visual_color=(0.3, 0.5, 0.2))

# add joints between the links
axisZ = (0, 0, 1)

origin = Frame.worldXY()
model.add_joint("joint1", Joint.CONTINUOUS, link0, link1, origin, axisZ)
model.add_joint("joint2", Joint.CONTINUOUS, link0, link2, origin, axisZ)
origin = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint3", Joint.CONTINUOUS, link2, link3, origin, axisZ)
model.add_joint("joint4", Joint.CONTINUOUS, link2, link4, origin, axisZ)
model.add_joint("joint5", Joint.CONTINUOUS, link4, link5, origin, axisZ)

# Create a configuration object matching the number of joints in your model
configuration = model.zero_configuration()
configuration = Configuration([(a1/180)*math.pi, (a2/180)*math.pi, (a3/180)*math.pi, (a4/180)*math.pi, (a5/180)*math.pi], [Joint.CONTINUOUS, Joint.CONTINUOUS, Joint.CONTINUOUS, Joint.CONTINUOUS, Joint.CONTINUOUS] , ["joint1", "joint2", "joint3", "joint4","joint5"])
# I don't know how to avoid having to copy paste Joints.CONTINUOUS five times. Also I don't understand why we should specify it again since it is supposed to be defined in the links
model.compute_transformations(configuration)

# Update the model using the artist
artist = Artist(model)
artist.update(configuration)

# Render everything
visual = artist.draw_visual()
artist.redraw()
