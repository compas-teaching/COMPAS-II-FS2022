"""Assignment 01: Project box to xy-plane
"""
from compas.geometry import Point, Vector, Plane
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Projection
from compas.artists import Artist
from compas.datastructures import Mesh

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame(Point(2, 2, 1), Vector(1, 0, 0), Vector(0, 1, 0.3))

# Create a Box with that frame
width, length, height = 1, 1, 1
box = Box(frame, width, length, height)

# Create a Projection (can be orthogonal, parallel or perspective)
plane = Plane([0,0,0],[0,0,1])
direction = [-1,-2,-1]
P = Projection.from_plane_and_direction(plane,direction)

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = mesh.transformed(P)

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh_projected)

# Draw
artist1.draw()
artist2.draw_edges(color=(0,255,0))
