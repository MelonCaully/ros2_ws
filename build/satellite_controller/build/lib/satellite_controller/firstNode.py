#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("nodeFirst")
        self.get_logger().info("Hello Mars")

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node) #keeps node alive
    rclpy.shutdown() 

if __name__ == '__main__':
    main()