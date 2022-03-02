from compas.robots import RobotModel

model = RobotModel.ur5(load_geometry=False)

# Get some relevant link names for FK
base = model.get_base_link_name()
endeffector = model.get_end_effector_link_name()
print(base)
print(endeffector)

# Create config
config = model.zero_configuration()

# Get FK for tip
print (model.forward_kinematics(config))
# Get FK for base
print (model.forward_kinematics(config, link_name=base))
