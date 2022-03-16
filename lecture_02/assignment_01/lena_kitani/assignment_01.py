"""Assignment 01: Project box to xy-plane
"""
from compas.geometry import Point
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Projection
from compas.artists import Artist
from compas.datastructures import Mesh
from compas.geometry import Transformation

# Define a Frame, which is not in the origin and a bit tilted to the world frame
pt, normal = Point(0, 1, 1), (0,0,1)
frame = Frame(pt, [0, -1,-0.3], [1, 2,3])

# Create a Box with that frame
width, length, height = 3,4,5
box = Box(frame, width, length, height)

# Create a Projection (can be orthogonal, parallel or perspective)
perspective = [1, 1, 0]
P = Projection.from_plane_and_point((pt, normal), perspective)
print("projection done")

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)
print(mesh)

# Apply the Projection onto the mesh
mesh_projected = mesh.transform(P)
print("mesh projected")
# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh_projected)

# Draw
artist1.draw()
artist2.draw_edges(color="#00ff00")

#i run the python -m compas_rhino.install in the anaconda prompt with the fs2022 activated but I still cannot get the results from the artist in rhino