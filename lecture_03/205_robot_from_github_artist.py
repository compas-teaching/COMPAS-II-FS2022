import compas
from compas.robots import GithubPackageMeshLoader
from compas.robots import RobotModel
from compas.artists import Artist

# Set high precision to import meshes defined in meters
compas.PRECISION = "12f"

# Select Github repository, package and branch where the model is stored
r = "ros-industrial/abb"
p = "abb_irb6600_support"
b = "kinetic-devel"

github = GithubPackageMeshLoader(r, p, b)
urdf = github.load_urdf("irb6640.urdf")

# Create robot model from URDF
model = RobotModel.from_urdf_file(urdf)

# Also load geometry
model.load_geometry(github)

# Draw model
artist = Artist(model, layer="Robot")
artist.clear_layer()
artist.draw_visual()
artist.redraw()
