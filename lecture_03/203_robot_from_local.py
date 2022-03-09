from compas.artists import Artist
from compas.robots import RobotModel

model = RobotModel.ur5(load_geometry=True)

artist = Artist(model, layer="Robot")
artist.clear_layer()
artist.draw_visual()
artist.redraw()
