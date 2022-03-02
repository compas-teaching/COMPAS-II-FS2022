from compas_fab.backends.kinematics.solvers import UR5Kinematics

from compas.geometry import Frame
from compas.robots import Configuration
from compas.robots import RobotModel

model = RobotModel.ur5(load_geometry=False)

f = Frame((0.417, 0.191, -0.005), (-0.000, 1.000, 0.00), (1.000, 0.000, 0.000))

solutions = UR5Kinematics().inverse(f)

for jv in solutions:
    print(Configuration.from_revolute_values(jv))
