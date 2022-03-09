from compas.artists import Artist
from compas.robots import RobotModel

model = RobotModel.ur5(load_geometry=True)

config = model.zero_configuration()
frame = model.forward_kinematics(config)

artist = Artist(frame)
artist.draw()

artist = Artist(model)
artist.update(config)
artist.draw()
