from compas_fab.backends import RosClient

from compas.robots import Configuration

with RosClient("localhost") as client:
    robot = client.load_robot()

    configuration = robot.zero_configuration()
    configuration.joint_values = (-0.106, 5.351, 2.231, -2.869, 4.712, 1.465)

    frame_WCF = robot.forward_kinematics(configuration)

    print("Frame in the world coordinate system")
    print(frame_WCF)
