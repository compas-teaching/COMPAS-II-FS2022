from compas.artists import Artist
from compas.robots import RobotModel

model = RobotModel.from_urdf_file("models/06_with_colors.urdf")
print model
artist = Artist(model, layer="Robot")
artist.clear_layer()
artist.draw_visual()
artist.redraw()

