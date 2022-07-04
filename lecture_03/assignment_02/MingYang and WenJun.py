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


# create cylinder in yz plane
radius, length = 0.3, 5
cylinder = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), length)
cylinder.transform(Translation.from_vector([length / 2.0, 0, 0]))

# create robot model
model = RobotModel("robot", links=[], joints=[])

# link meshes (calling Mesh.from_shape effectively creates a copy of the shape)
mesh = Mesh.from_shape(cylinder)

# n refines hilbert num

def config_data(n):
    hilbert_seq = "a"
    link_num = int(math.pow(4,n)-1)
    for _ in range(n):
        new_seq = ""
        for char in hilbert_seq:
            if char == "a":
                new_seq += "-bF+aFa+Fb-"
            elif char == "b":
                new_seq += "+aF-bFb-Fa+"
            else:
                new_seq += char
        hilbert_seq = new_seq

    fix = ''
    for i,char in enumerate(hilbert_seq):
        if char != 'a' and char != 'b' :
            fix +=char

    fix = fix.replace('+-', '')
    fix = fix.replace('-+', '')

    final = ''
    for k,char in enumerate(fix):
        if char == "F":
            if k == 0:
                final+='0'
            else:
                former = fix[k-1]
                if former == "F":
                    final+='0'
        else:
            final+=char

    return final

# It takes forever if n>5
data = config_data(3)

# add links
link0 = model.add_link("world")
link_list = [link0]
for i in range(1,len(data)+1):
    link = model.add_link("link"+ str(i), visual_mesh=mesh, visual_color=(0,1 - 1/len(data)*i,1/len(data)*i))
    link_list.append(link)

# add joints between the links
axis = (0, 0, 1)

origin = Frame.worldXY()
model.add_joint("joint0", Joint.CONTINUOUS, link_list[0], link_list[1], origin, axis)
joints = ["joint0"]

for i in range(1,len(data)):
    origin = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
    model.add_joint("joint"+str(i), Joint.CONTINUOUS, link_list[i], link_list[i+1], origin, axis)
    joints.append("joint"+str(i))


# Create a configuration object matching the number of joints in your model
joint_values = []

for i, char in enumerate(data):
    if char == '-':
        joint_values.append(math.pi/2)
    elif char == '+':
        joint_values.append(-math.pi/2)
    else:
        joint_values.append(0)

configuration = model.zero_configuration()
configuration.joint_values = joint_values

# Update the model using the artist
artist = Artist(model)
artist.update(configuration)

# Render everything
artist.clear()
artist.draw_visual()
artist.redraw()
