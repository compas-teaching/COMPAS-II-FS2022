"""Assignment 01: Project box to xy-plane
"""
from compas.geometry import Box
from compas.geometry import Vector
from compas.geometry import Point
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection
from compas.artists import Artist
from compas.datastructures import Mesh

# Define a Frame, which is not in the origin and a bit tilted to the world frame

frame = Frame(Point(10,10,10), Vector(1,1,0), Vector(0,1,1))

# Create a Box with that frame
width, length, height = 5,5,5
box = Box(frame, width, length, height)

# Create a Projection (can be orthogonal, parallel or perspective)
point_a = [0,0,0]
point_b = [15,15,15]
normal = [0,0,1]
direction = [0, 3, -1]
plane = Plane(point_a, normal)


P_orth = Projection.from_plane(plane)
P_para = Projection.from_plane_and_direction(plane, direction)
P_pers = Projection.from_plane_and_point(plane, point_b)

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected_orth = mesh.transformed(P_orth)
mesh_projected_para = mesh.transformed(P_para)
mesh_projected_pers = mesh.transformed(P_pers)

# Create artists
artist1 = Artist(frame)
artist2 = Artist(box)
artist_orth = Artist(mesh_projected_orth)
artist_para = Artist(mesh_projected_para)
artist_pers = Artist(mesh_projected_pers)

# Draw
artist1.draw()
artist2.draw()
artist_orth.draw_edges(color=[255,0,0])
artist_para.draw_edges(color=[0,255,0])
artist_pers.draw_edges(color=[0,0,255])


