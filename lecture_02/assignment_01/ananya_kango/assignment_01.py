"""Assignment 01: Project box to xy-plane
"""

from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Projection
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Plane

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame([15,15,15],[1.25,1.5,2.5],[0,1,0])

# Create a Box with that frame
box = Box(frame,xsize=5,ysize=5,zsize=3.5)

# Create a Projection (can be orthogonal, parallel or perspective)
P1 = Projection.from_plane(Plane.worldXY()) #orthogonal
P2 = Projection.from_plane_and_direction(Plane.from_frame(Frame.worldZX()),[0,1,0]) #parallel
P3 = Projection.from_plane_and_point(Plane.from_frame(Frame.worldYZ()),[45,15,15]) #perspective

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected_a = mesh.transformed(P1)
mesh_projected_b = mesh.transformed(P2)
mesh_projected_c = mesh.transformed(P3)

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh_projected_a)
artist3 = Artist(mesh_projected_b)
artist4 = Artist(mesh_projected_c)

# Draw
artist1.draw(color=[20,20,20])
artist2.draw_edges(color=[255, 0, 93])
artist3.draw_edges(color=[0, 94, 255])
artist4.draw_edges(color=[194, 72, 2])

