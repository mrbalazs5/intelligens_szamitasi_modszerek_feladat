# intelligens_szamitasi_modszerek_feladat

## Task

Create a ROS 2 Python application with 2 turtles following each other.

## Run

In the root folder run:
- source /opt/ros/foxy/setup.bash
- colcon build
- ros2 run turtlesim turtle_teleop_key

In a new terminal:
- source /opt/ros/foxy/setup.bash
- . install/local_setup.bash
- ros2 launch int_szam_mod_feladat int_szam_mod_feladat.launch.py
