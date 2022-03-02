from compas_fab.backends.interfaces import ClientInterface
from compas_fab.backends.kinematics import AnalyticalInverseKinematics
from compas_fab.backends.kinematics.solvers import OffsetWristKinematics
from compas_fab.robots import Robot

from compas.geometry import Frame
from compas.robots import RobotModel

model = RobotModel.ur5(load_geometry=False)

client = ClientInterface()
client.inverse_kinematics = AnalyticalInverseKinematics()
client.inverse_kinematics.planner = OffsetWristKinematics([
  0.089159, # d1
 -0.42500,  # a2
 -0.39225,  # a3
  0.10915,  # d4
  0.09465,  # d5
  0.0823,   # d6
])

f = Frame((0.417, 0.191, -0.005), (-0.000, 1.000, 0.00), (1.000, 0.000, 0.000))

robot = Robot(model, client=client)
solutions = robot.iter_inverse_kinematics(f)

for jv in solutions:
    print(jv)
