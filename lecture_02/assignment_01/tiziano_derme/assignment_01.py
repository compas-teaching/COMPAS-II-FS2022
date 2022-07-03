"""Assignment 01: Project box to xy-plane
"""
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Projection
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Plane

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame([2, 2, 2], [0.978, 0.010, -0.210], [0.090, 0.882, 0.463])


# Create a Box with that frame
box = Box(frame, 1.5, 1.5, 1.5)

# Create a Projection (can be orthogonal, parallel or perspective)
point = [0,0,0]
normal = [0,0,1]
plane = Plane(point, normal)
P = Projection.from_plane(plane)

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = Mesh.transformed(mesh,P)

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh_projected)

# Draw
artist1.draw()
artist2.draw_edges(color="#00ff00")
