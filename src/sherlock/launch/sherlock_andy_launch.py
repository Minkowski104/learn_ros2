from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sherlock',
            namespace='sherlock',
            executable='sherlock1'
        ),
        Node(
            package='sherlock',
            namespace='sherlock2',
            executable='sherlock2'
        ),
        Node(
            package='sherlock',
            namespace='anderson',
            executable='anderson'
        ),
    ])