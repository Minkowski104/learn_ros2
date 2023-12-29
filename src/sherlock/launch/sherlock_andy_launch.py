from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sherlock',
            executable='sherlock1'
        ),
        Node(
            package='sherlock',
            executable='sherlock2'
        ),
        Node(
            package='sherlock',
            executable='anderson'
        ),
    ])