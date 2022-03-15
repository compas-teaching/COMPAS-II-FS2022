from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Projection
from compas.artists import Artist
from compas.datastructures import Mesh

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame =Frame([3, 3, 3], [0.45, 0.1, 0.8], [6, 3, 0])

# Create a Box with that frame
width, length, height = 2, 3, 4
box = Box(frame, width, length, height)

# Create a Projection (can be orthogonal, parallel or perspective)
perspective = [1, 1, 1]
point, normal = [0, 0, 0], [0, 0, 1]
P = Projection.from_plane_and_point((point, normal), perspective)
print(P)

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = mesh.transformed(P)
print(mesh_projected)

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh_projected)

# Draw
artist1.draw()
artist2.draw_edges(color="#00ff00")
