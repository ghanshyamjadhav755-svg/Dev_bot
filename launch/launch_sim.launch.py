import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():

    package_name = 'my_bot'

    # ----------------------------------------
    # Robot State Publisher
    # ----------------------------------------
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory(package_name),
                'launch',
                'rsp.launch.py'
            )
        ]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    # ----------------------------------------
    # Gazebo Server + Client
    # ----------------------------------------
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            )
        ])
    )

    # ----------------------------------------
    # Spawn Robot Entity
    # ----------------------------------------
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'my_bot',
            '-x', '0.5',
            '-y', '0.5',
            '-z', '0.05'
        ],
        output='screen'
    )

    # ----------------------------------------
    # RViz2 with Config File
    # ----------------------------------------
    rviz_config_path = os.path.join(
        get_package_share_directory(package_name),
        'config',
        'view_bot.rviz'
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_path],
        output='screen'
    )

    # ----------------------------------------
    # Launch Description
    # ----------------------------------------
    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
        rviz_node,
    ])

