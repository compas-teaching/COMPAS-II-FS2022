"""Assignment 01: Project box to xy-plane
"""
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection

from compas.artists import Artist
from compas.datastructures import Mesh

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame_0 = Frame([3.,9.0,5.],[1.,2.,3.],[-3.,-1.,1.])

# Create a Box with that frame
box = Box(frame_0,1.,1.,1.)

# Create a Projection (can be orthogonal, parallel or perspective)
T = Projection.from_plane_and_direction(Plane.worldXY(),[2.,-1.,-1.])

# Create a Mesh from the Box
mesh_box = Mesh.from_shape(box)

# Apply the Projection onto the mesh
box_pro = mesh_box.transformed(T)

# Create artists
artist1 = Artist(box)
artist2 = Artist(box_pro)

# Draw
artist1.draw()
artist2.draw_edges(color="#00ff00")
