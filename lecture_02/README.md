# COMPAS II: Robotic fundamentals

Introduction to robotics: 1) anatomy of an industrial robot, 2) frames and coordinate systems, 3) transformations.

Brief intro to kinematic functions and path planning.

👉 [Slides](lecture_02.pdf)
📜 [Assignment 01](assignment_01/README.md)

## Examples

* Frame
  * [Construct a frame](101_several_ways_to_construct_frame.py)
  * [Point in frame](102_point_in_frame.py)
  * [Frame in frame](103_frame_in_frame.py)
  * [Box from world to local](104_box_from_the_world_to_local.py)
  * [Box from world to local: visualization](105_box_from_the_world_to_local_artist.py)

* Transformation
  * [Examples](106_examples_transformation.py)
  * [Inverse transformation](107_inverse_transformation.py)
  * [Pre-multiplication](108_premultiply_transformations.py)
  * [Pre vs post multiplication](109_pre_vs_post_multiplication.py)
  * [Matrix decomposition](110_decompose_transformation.py)
  * [Transform point and vector](111_transform_point_and_vector.py)
  * [Transform multiple](112_transform_multiple.py)
  * [Change of basis](113_change_basis_transformation.py)
  * [Transformations: interactive in GH](113_change_basis_and_transformation_between_frames.ghx)
  * [Transform between frames](114_transformation_between_frames.py)
  * [Box from world to local: visualization](115_box_from_the_world_to_local_artist.py)

* Rotation
  * [Construct a rotation](116_several_ways_to_construct_rotation.py)
  * [Robot TCP orientations](117_robot_tcp_orientations.py)
  * [Rotations: interactive in GH](118_rotations.ghx)
  * [Euler angles](118_euler_angles.py)
  * [Axis angle](119_axis_angle.py)
  * [Quaternions](120_quaternion.py)

* Intro to kinematics
  * [Joint types](211_joint_types.py)
  * [Configuration](212_configuration.py)
  * [Forward kinemativs](213_forward_kinematics.py)
  * [Forward kinematics: visualization](214_forward_kinematics_artist.py)
  * [Inverse kinematics](215_inverse_kinematics.py)
  * [Inverse kinematics: visualization](216_inverse_kinematics_artist.py)
  * [Inverse kinematics: interactive in GH](217_inverse_kinematics.ghx)
  * [Inverse kinematics: custom solver from DH parameters](218_inverse_kinematics_dh_params.py)
