import rclpy
from rclpy.node import Node
from canopen import *

class MotorController(Node):
    def __init__(self):
        #Node.get_node_names_and_namespaces()
        super().__init__('Subscriber')
        self.get_logger().info(str(self.get_name()))

        ###################
        # CANopen network #
        ###################

        network = canopen.Network()
        network.connect(channel='can1', bustype='socketcan')

        ###########################
        # Setup motor controllers #
        ###########################

        self.node = network.add_node(Node_ID, 'src/motor_controller/config/C5-E-2-09.eds')

def main():
    rclpy.init()
    node = MotorController()
    rclpy.spin(node)
    rclpy.shutdown()
    