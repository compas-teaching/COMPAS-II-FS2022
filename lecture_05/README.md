# COMPAS II: Path planning for pick and place processes

Planning scene operations.

Cartesian and kinematic path planning using MoveIt.

End effectors.

Method for Pick and Place planning.

👉 [Slides](lecture_05.pdf)

## Examples

Make sure you start (`compose up`) the container with a UR3e planner for these examples.

* Planning scene in MoveIt
  * [Planning scene preview in GH](314_planning_scene.ghx)
  * [Add objects to the scene](315_add_collision_mesh.py)
  * [Append nested objects to the scene](316_append_collision_meshes.py)
  * [Remove objects from the scene](317_remove_collision_mesh.py)

* End effectors (tool)
  * [Attach tool](400_attach_tool.py)
  * [Detach tool](401_detach_tool.py)

* Path planning
  * [Cartesian motion planning](410_plan_cartesian_motion_ros.py)
  * [Cartesian motion planning with tool](411_plan_cartesian_motion_ros_with_tool.py)
  * [Free space motion planning](412_plan_motion_ros.py)
  * [Free space motion planning with tool](413_plan_motion_ros_with_tool.py)
  * [Constraints](414_constraints.py)

* Pick and Place
  * [Pick and Place skeleton](420_pick_and_place.py)
  * [Pick and Place skeleton in GH](421_pick_and_place_artist.ghx)

## Preparation for next lecture

* No coding assignment, but:
* **Use and experiment** with example 420:
  * To search paths for more than one part
  * To add the current part as attached collision mesh
* **Pair and Answer** the following two questions:
  * What was the most important thing you learned today?
  * What important question(s) remain(s) unanswered?
