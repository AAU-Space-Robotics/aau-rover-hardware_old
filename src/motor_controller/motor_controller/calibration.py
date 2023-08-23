import rclpy
from rclpy.node import Node

class CalibrationController(Node):
    def __init__(self):
        #Node.get_node_names_and_namespaces()
        super().__init__('Publicher')
        self.get_logger().info('Calib Hello World')


def main():
    rclpy.init()
    node = CalibrationController()
    rclpy.spin(node)
    rclpy.shutdown()
    