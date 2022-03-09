from compas.robots import GithubPackageMeshLoader
from compas.robots import RobotModel

# Select Github repository, package and branch where the model is stored
r = "ros-industrial/abb"
p = "abb_irb6600_support"
b = "kinetic-devel"

github = GithubPackageMeshLoader(r, p, b)
urdf = github.load_urdf("irb6640.urdf")

# Create robot model from URDF
model = RobotModel.from_urdf_file(urdf)

print(model)
