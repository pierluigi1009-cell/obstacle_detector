import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import numpy as np
import math

class ObstacleClusters(Node):
    def __init__(self):
        super().__init__('obstacle_clusters')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)
        self.distance_threshold = 0.2  # [m] distance max entre deux points d’un même obstacle
        self.min_distance = 0.1        # [m] distance minimale à considérer
        self.max_distance = 1.0        # [m] distance maximale à considérer (⟵ changée à 1 mètre)
        self.get_logger().info("detection des Obstacles à moin de  1 m")

    def scan_callback(self, msg):
        ranges = np.array(msg.ranges)
        angles = msg.angle_min + np.arange(len(ranges)) * msg.angle_increment

        # Garder uniquement les valeurs valides
        valid_mask = (ranges > msg.range_min) & (ranges < msg.range_max)
        ranges = ranges[valid_mask]
        angles = angles[valid_mask]

        # Filtrer selon les distances d’intérêt (ici < 1 m)
        useful_mask = (ranges > self.min_distance) & (ranges < self.max_distance)
        ranges = ranges[useful_mask]
        angles = angles[useful_mask]

        if len(ranges) == 0:
            self.get_logger().info("Aucun obstacle à moins de 1 m.")
            return

        # Détection des clusters
        clusters = []
        current_cluster = [0]
        for i in range(1, len(ranges)):
            dist_diff = abs(ranges[i] - ranges[i-1])
            if dist_diff < self.distance_threshold:
                current_cluster.append(i)
            else:
                clusters.append(current_cluster)
                current_cluster = [i]
        clusters.append(current_cluster)

        # Moyenne de chaque cluster
        obstacle_list = []
        for cluster in clusters:
            r_mean = np.mean(ranges[cluster])
            a_mean = np.mean(angles[cluster])
            obstacle_list.append((r_mean, a_mean))

        # Affichage
        self.get_logger().info(f"{len(obstacle_list)} obstacle(s) détecté(s) à moins de 1m :")
        for i, (r, a) in enumerate(obstacle_list):
            x = r * math.cos(a)
            y = r * math.sin(a)
            self.get_logger().info(f"   Obstacle {i+1}: {r:.2f} m @ {math.degrees(a):.1f}°  (x={x:.2f}, y={y:.2f})")


def main(args=None):
    rclpy.init(args=args)
    node = ObstacleClusters()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

