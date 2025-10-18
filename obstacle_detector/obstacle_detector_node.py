import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math

class ObstacleDetector(Node):
    def __init__(self):
        super().__init__('obstacle_detector')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)
        self.threshold_distance = 0.5  # [m]
        self.get_logger().info("Début de la detect")

    def scan_callback(self, msg):
        # Filtrer les distances valides
        valid_ranges = [r for r in msg.ranges if msg.range_min < r < msg.range_max]

        if not valid_ranges:
            self.get_logger().warn("Valeur abérrante")
            return

        min_dist = min(valid_ranges)

        if min_dist < self.threshold_distance:
            self.get_logger().warn(f" Obstacle détecté à {min_dist:.2f} m !")
        else:
            self.get_logger().info(f" Rien détécté (distance min = {min_dist:.2f} m)")

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleDetector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
