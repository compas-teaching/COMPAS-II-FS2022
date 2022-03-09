from compas.artists import Artist
from compas.robots import LocalPackageMeshLoader
from compas.robots import RobotModel

model = RobotModel.from_urdf_file("models/05_origins_meshes.urdf")

loader = LocalPackageMeshLoader("models", "basic")
model.load_geometry(loader)

artist = Artist(model, layer="Robot")
artist.clear_layer()
artist.draw_visual()
artist.redraw()
