"""Assignment 01: Project box to xy-plane
"""
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Projection
from compas.geometry import Plane
from compas.artists import Artist
from compas.datastructures import Mesh

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame([0,20,30], [20,0,40], [0,10,50])

# Create a Box with that frame
box = Box(frame, 30, 40, 20)

# Create a Projection (can be orthogonal, parallel or perspective)
P_orth = Projection.from_plane(Plane([0,0,0],[0,0,1]))
P_par = Projection.from_plane_and_direction(Plane([0,0,0],[0,0,1]),[0,3,-1])
P_per = Projection.from_plane_and_point(Plane([0,0,0],[0,0,1]), [30,45,60])

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = mesh.transformed(P_per)

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh_projected)

# Draw
artist1.draw()
artist2.draw_edges(color=[0,0,255])

