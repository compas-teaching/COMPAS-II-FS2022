"""Example: Bring a box from the world coordinate system into another coordinate
system and view in Rhino.
"""
from compas.artists import Artist
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Transformation

# Box in the world coordinate system
frame = Frame([1, 0, 0], [-0.45, 0.1, 0.3], [1, 0, 0])
width, length, height = 1, 1, 1
box = Box(frame, width, length, height)

# Frame F representing a coordinate system
F = Frame([2, 2, 2], [0.978, 0.010, -0.210], [0.090, 0.882, 0.463])

# Get transformation between world and frame F
# T = ...
# Apply transformation on box.
# box_transformed = ...
print("Box frame transformed", box_transformed.frame)

# create artists
artist1 = Artist(Frame.worldXY())
artist2 = Artist(box)
artist3 = Artist(F)
artist4 = Artist(box_transformed)

# draw
artist1.draw()
artist2.draw()
artist3.draw()
artist4.draw()
