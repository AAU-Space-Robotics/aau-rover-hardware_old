from launch import LaunchDescription
from launch.event_handlers import (OnProcessStart)
from launch_ros.actions import Node
from launch.actions import (LogInfo, RegisterEventHandler, ExecuteProcess)

from launch.substitutions import FindExecutable

calibration = Node(
            package='motor_controller',
            executable='calibration',
        )

Front_Left = Node(
            package='motor_controller',
            namespace='Wheel_Steering',
            executable='motor',
            name='Front_Left',
        )

Front_Right = Node(
            package='motor_controller',
            namespace='Wheel_Steering',
            executable='motor',
            name='Front_Right',
        )

Rear_Left = Node(
            package='motor_controller',
            namespace='Wheel_Steering',
            executable='motor',
            name='Rear_Left',
        )

Rear_Right = Node(
            package='motor_controller',
            namespace='Wheel_Steering',
            executable='motor',
            name='Rear_Right',
        )

def generate_launch_description():
    return LaunchDescription([

        Front_Left, 
        Front_Right, 
        Rear_Left, 
        Rear_Right,

        RegisterEventHandler(
            OnProcessStart(
                target_action= Front_Left,
                handle_once=True,
                on_start=[
                    LogInfo(msg='Calibrating steering wheels'),
                    calibration,
                ]

            )
        ),

        Node(
            package='motor_controller',
            namespace='Wheel_Linear',
            executable='motor',
            name='Front_Left',
        ),
        Node(
            package='motor_controller',
            namespace='Wheel_Linear',
            executable='motor',
            name='Front_Right',
        ),
        Node(
            package='motor_controller',
            namespace='Wheel_Linear',
            executable='motor',
            name='Center_Left',
        ),
        Node(
            package='motor_controller',
            namespace='Wheel_Linear',
            executable='motor',
            name='Center_Right',
        ),
        Node(
            package='motor_controller',
            namespace='Wheel_Linear',
            executable='motor',
            name='Rear_Left',
        ),
        Node(
            package='motor_controller',
            namespace='Wheel_Linear',
            executable='motor',
            name='Rear_Right',
        )
    ])