"""Assignment 01: Project box to xy-plane
"""
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Projection
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Plane

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame([0.0, 3.0, 15], [2.0, 1.0, 1.0],[-1.0, 2.0, 1.0])

# Create a Box with that frame
box = Box(frame, 10, 10, 10)
# Create a Projection (can be orthogonal, parallel or perspective)
P = Projection.from_plane(Plane([0,0,0], [0,0,1]))

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
