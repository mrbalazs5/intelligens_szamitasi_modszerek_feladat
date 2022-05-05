import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node


def generate_launch_description():
    demo_nodes = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('int_szam_mod_feladat'), 'launch'),
            '/int_szam_mod_feladat.launch.py']),
        launch_arguments={'target_frame': 'carrot1'}.items(),
        )

    return LaunchDescription([
        demo_nodes,
        Node(
            package='int_szam_mod_feladat',
            executable='fixed_frame_tf2_broadcaster',
            name='fixed_broadcaster',
        ),
    ])
