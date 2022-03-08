"""Assignment 01: Project box to xy-plane
"""
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Projection
from compas.artists import Artist
from compas.datastructures import Mesh

point = [2.3,3.3,4]
vector_1 = [1.1,2.0,0.9]
vector_2 = [1.2,2.1,1.2]
plane = [(0,0,0), (0,0,1)]

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame(point,vector_1,vector_2)

# Create a Box with that frame
box = Box(frame,3.14,4,2)

# Create a Projection (can be orthogonal, parallel or perspective)
##orthogonal
#P = Projection.from_plane(plane)

##parallel
P = Projection.from_plane_and_direction(plane,[0,1,1])

##perspective
#P = Projection.from_plane_and_point(plane,[0,1,1])

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = mesh.transformed(P)

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh_projected)

# Draw
artist1.draw()
artist2.draw_edges(color="#00ff00")
