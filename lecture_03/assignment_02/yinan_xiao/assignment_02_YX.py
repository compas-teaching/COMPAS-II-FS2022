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

#import rhinoscriptsyntax as rs
#objects = rs.ObjectsByLayer("Default")
#rs.DeleteObjects(objects)

# create cylinder in yz plane
radius, length = 0.3, 5
cylinder = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), length)
cylinder.transform(Translation.from_vector([length / 2.0, 0, 0]))

radius3, length3 = 0.3, 10
cylinder3 = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius3), length3)
cylinder3.transform(Translation.from_vector([length3 / 2.0, 0, 0]))

# create robot model
model = RobotModel("robot", links=[], joints=[])

# link meshes (calling Mesh.from_shape effectively creates a copy of the shape)
mesh1 = Mesh.from_shape(cylinder)
mesh2 = Mesh.from_shape(cylinder)
mesh3 = Mesh.from_shape(cylinder3)

# add links
link0 = model.add_link("world")
link1 = model.add_link("link1", visual_mesh=mesh1, visual_color=(0.2, 0.5, 0.6))
link2 = model.add_link("link2", visual_mesh=mesh2, visual_color=(0.5, 0.6, 0.2))
link3 = model.add_link("link3", visual_mesh = mesh3)
link4 = model.add_link("link4", visual_mesh = mesh3)

# add joints between the links
axis = (0, 0, 1)

origin = Frame.worldXY()
model.add_joint("joint1", Joint.CONTINUOUS, link0, link1, origin, axis)

origin = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint2", Joint.CONTINUOUS, link1, link2, origin, axis)

origin = Frame((length, 0, 0), (0.87, -0.5, 0), (0.5, 0.87, 0))
model.add_joint("joint3", Joint.CONTINUOUS, link2, link3, origin, axis)

origin = Frame((length, 0, 0), (0.87, 0.5, 0), (-0.5, 0.87, 0))
model.add_joint("joint4", Joint.CONTINUOUS, link2, link4, origin, axis)

# Create a configuration object matching the number of joints in your model
# configuration = ....
config = Configuration([Joint.CONTINUOUS, Joint.CONTINUOUS, Joint.CONTINUOUS, Joint.CONTINUOUS], ["joint1", "joint2", "joint3", "joint4"])
print(config)

# Update the model using the artist
artist = Artist(model)
# artist.update ...

# Render everything
artist.clear_layer()
artist.draw_visual()
artist.redraw()