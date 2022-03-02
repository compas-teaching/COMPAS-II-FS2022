# Units:
#  - Revolute joint : radiants
#  - Prismatic joint: meters

import math
from compas.robots.model import Joint
from compas.robots import Configuration

print('Default constructor (radians & meters!)')
config = Configuration([math.pi, 4], [Joint.REVOLUTE, Joint.PRISMATIC], ['joint_1', 'ext_axis_1'])
print(config)

print()
print('Construct from revolute values')
config = Configuration.from_revolute_values([math.pi, 0], ['joint_1', 'joint_2'])
print(config)

print()
print('Construct from prismatic & revolute values')
config = Configuration.from_prismatic_and_revolute_values([4], [math.pi], ['ext_axis_1', 'joint_1'])
print(config)

print()
print('Merge two configurations')
config_a = Configuration([4], [Joint.PRISMATIC], ['ext_axis_1'])
config_b = Configuration([math.pi], [Joint.REVOLUTE], ['joint_1'])
config_c = config_a.merged(config_b)
print(config_c)

print()
print('Access and update of configuration')
config = Configuration.from_revolute_values([math.pi, 0], ['joint_1', 'joint_2'])
print('Joint 1: {:.3f}, Joint 2: {:.3f}'.format(config['joint_1'], config['joint_2']))
config['joint_1'] = math.pi / 2
config['joint_2'] = math.pi
print(config)
