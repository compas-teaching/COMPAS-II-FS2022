import compas
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Projection
from compas.artists import Artist
from compas.datastructures import Mesh

compas.DATA = "/Users/Maxence/opt/anaconda3/envs/fs2022/lib/python3.8/site-packages/compas/data/samples/"

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame([1, 3, 4.6], [-0.45, 3.1, 0.3], [1, 2, 1])

# Create a Box with that frame
width, length, height = 1.5, 3, 2
box = Box(frame, width, length, height)

# Create a Projection (can be orthogonal, parallel or perspective)
OriginOfProjectionPlane = [0, 0, 0]
NormalOfProjectionPlane = [0, 0, 1]
ProjectionPlane = (OriginOfProjectionPlane, NormalOfProjectionPlane)
DirectionOfProjection = [1, 2, -3]
ProjectionTransformation = Projection.from_plane_and_direction(ProjectionPlane, DirectionOfProjection)

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = mesh.transformed(ProjectionTransformation)

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh_projected)

# Draw
artist1.draw()
artist1.redraw()
artist2.draw_edges(color="#00ff00")
# Color doesn't appear green in my shaded viewport (appears black regarless of the HEX value)
# Another appearance issue I have on mac is the RobotArtist in grasshopper doesn't display edges, just a plain color, no shade.
artist2.redraw()
