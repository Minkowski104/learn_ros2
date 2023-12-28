from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sherlock',
            executable='publisher',
        ),
        # Node(
        #     package='week0_tutorials',
        #     executable='subscriber',
        # ),
    ])