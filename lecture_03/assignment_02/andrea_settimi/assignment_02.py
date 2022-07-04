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
import time


# create cylinder in yz plane
radius, length = 0.3, 5
cylinder = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), length)
cylinder.transform(Translation.from_vector([length / 2.0, 0, 0]))
mesh = Mesh.from_shape(cylinder)

# create robot model
model = RobotModel("robot", links=[], joints=[])

# add links
n_links = 100

link0 = model.add_link("link0")
for l in range(1, n_links-1):
    model.add_link(name=("link" + str(l)), visual_mesh=mesh, visual_color=(l/n_links, 0, l/n_links))
linkN = model.add_link(("link" + str(n_links)))

print(len(model.links))

# test add joints
axis = (0, 0, 1)

links = model.links

origin = Frame((0, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint0", Joint.CONTINUOUS, links[0], links[1], origin, axis)

origin = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))

for j in range(2, n_links):
    joint_name = "joint1" + str(j)
    joint_type = Joint.CONTINUOUS
    joint_parent = links[j]
    joint_child = links[j-1]

    model.add_joint(joint_name, Joint.CONTINUOUS, joint_child, joint_parent, origin, axis)

# Create a configuration object matching the number of joints in your model
config = model.zero_configuration()

# Create a double spiral path with a new configuration and show animation
for i in range(n_links-1):
    config.joint_values[i] = (i/(n_links-1))*2*3.14
    artist = Artist(model)
    artist.update(config)
    artist.clear()
    artist.draw_visual()
    artist.redraw()
    time.sleep(0.001)
