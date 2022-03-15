"""Assignment 01: Project box to xy-plane
"""
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Projection
from compas.geometry import Plane
from compas.artists import Artist
from compas.datastructures import Mesh

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame =Frame([1,9,7],[-0.5,0.5,0.5],[0.5,0.4,0.2])

# Create a Box with that frame
box = Box(frame, 2, 2, 2)

# Create a Projection (can be orthogonal, parallel or perspective)
plane = Plane([0,0,0],[0,0,1])
P1 = Projection.from_plane(plane)
P2 = Projection.from_plane_and_direction(plane,[0,1,1])
P3 = Projection.from_plane_and_point(plane, [50,50,50])

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected_1 = mesh.transformed(P1)
mesh_projected_2 = mesh.transformed(P2)
mesh_projected_3 = mesh.transformed(P3)

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh_projected_1)
artist3 = Artist(mesh_projected_2)
artist4 = Artist(mesh_projected_3)

# Draw
artist1.draw()
artist2.draw_edges(color=[0, 255, 255])
artist3.draw_edges(color=[255, 0, 255])
artist4.draw_edges(color=[255, 255, 0])



