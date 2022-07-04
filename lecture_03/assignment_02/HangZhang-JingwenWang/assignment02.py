"""Assignment 02: Build your own robot model
"""
from compas.utilities import pairwise
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Circle
from compas.geometry import Cylinder
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Translation
from compas.geometry import Point, Vector
from compas.robots import Configuration
from compas.robots import Joint
from compas.robots import RobotModel
import random
import math

### The goal of this script is to create Logarithmic spiral shape
### Author: Jingwen Wang & Hang Zhang
### 2022.03.13

# create robot model
model = RobotModel("robot", links=[], joints=[])

# record all the parameters
a, b = 1, 0.2
point = Point(0,0,0)
theta = 0.4 * math.pi
length_list = [] #n-1
point_list = [] #n
vector_list = [] #n-1
n = 20 #number of segments

for i in range(n):
    r = a*math.pow(math.e,b*(i+1)*theta)
    new_point = Point(r*math.cos((i+1)*(theta)), r*math.sin((i+1)*(theta)),0)
    if i!=0:
        vector = new_point - point
        length_list.append(vector.length)
        vector_list.append(vector)
    point = new_point
    point_list.append(new_point)

#Create links
link_list = [] #n
link_list.append(model.add_link("world"))

for i,length in enumerate(length_list):
    radius = 0.3
    cylinder = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), length)
    cylinder.transform(Translation.from_vector([length / 2.0, 0, 0]))
    mesh = Mesh.from_shape(cylinder)
    #mesh_list.append(mesh)
    link_list.append(model.add_link("link"+str(i), visual_mesh=mesh, visual_color=(random.random(), random.random(), random.random())))

#Create joints
angle_list = []
angle_list.append(0.0) #n-2

axis = (0, 0, 1)
#add the world list
origin = Frame.worldXY()
model.add_joint("joint0", Joint.CONTINUOUS, link_list[0], link_list[1], origin, axis)

#iterate through n-2 times
for i, (vector1,vector2) in enumerate(pairwise(vector_list)):
    angle_list.append(vector1.angle(vector2))
    origin = Frame((length_list[i], 0, 0), (1, 0, 0), (0, 1, 0))
    model.add_joint("joint"+str(i+1), Joint.CONTINUOUS, link_list[i+1], link_list[i+2], origin, axis)

# Create a configuration object matching the number of joints in your model
configuration = model.zero_configuration()
configuration.joint_values = angle_list

# Update the model using the artist
artist = Artist(model)
artist.update(configuration)

# Render everything
artist.draw_visual()
artist.redraw()
