from compas.geometry import Box, Frame, Projection, Plane
from compas.artists import Artist
from compas.datastructures import Mesh

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame.from_points([0,0,0], [1,9,-2], [9,-3,-6])

# Create a Box with that frame
len, wid, hei = 2, 6, 8
box = Box(frame, len, wid, hei)

# Create a Projection (can be orthogonal, parallel or perspective)
proj_plane = Plane.from_frame(Frame.from_points([-3.413,13.422,-6.286], [-3.614,26.970,-7.904], [-10.881,13.422,-5.362]))
proj_vect = [-2.42,16.18,-3.80]
P = Projection.from_plane_and_direction(proj_plane, proj_vect)

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = mesh.transformed(P)

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh_projected)

# Draw
artist1.draw(color=[0,255,255])
artist2.draw_edges(color=[255,0,255])
