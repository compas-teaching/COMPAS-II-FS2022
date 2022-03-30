# COMPAS II: ROS & MoveIt in the design environment

Introduction to ROS, topics, services, actions.

Basic inter-process communication via ROS nodes. Reproducible ROS environments with Docker.

Robot planning: forward and inverse kinematic functions, cartesian and kinematic planning. MoveIt integration in the parametric design environment.

👉 [Slides](lecture_04.pdf)
📜 [Assignment 03](assignment_03/README.md)

## Examples

* ROS Basics
  * [Verify connection](301_check_connection.py)
  * [Interconnected nodes: Listener](302_ros_hello_world_listener.py)
  * [Interconnected nodes: Talker](303_ros_hello_world_talker.py)
  * [Interconnected nodes: Talker in GH](304_ros_hello_world_talker.ghx)

* ROS & MoveIt planning
  * [Load robot](305_robot_from_ros.py)
  * [Load robot: visualization](306_robot_from_ros_artist.py)
  * [Forward Kinematics](307_forward_kinematics_ros.py)
  * [Inverse Kinematics](308_inverse_kinematics_ros.py)
  * [Cartesian motion planning](309_plan_cartesian_motion_ros.py)
  * [Cartesian motion planning: visualization](310_plan_cartesian_motion_ros_artist.py)
  * [Free space motion planning](311_plan_motion_ros.py)
  * [Free space motion planning: visualization](312_plan_motion_ros_artist.py)
  * [Constraints](313_constraints.py)

* Planning scene in MoveIt
  * [Planning scene preview in GH](314_planning_scene.ghx)
  * [Add objects to the scene](315_add_collision_mesh.py)
  * [Append nested objects to the scene](316_append_collision_meshes.py)
  * [Remove objects from the scene](317_remove_collision_mesh.py)

