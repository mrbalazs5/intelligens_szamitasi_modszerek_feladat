from geometry_msgs.msg import PointStamped
from geometry_msgs.msg import Twist

import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose
from turtlesim.srv import Spawn


class PointPublisher(Node):

    def __init__(self):
        super().__init__('turtle_tf2_message_broadcaster')

        self.spawner = self.create_client(Spawn, 'spawn')
        self.turtle_spawning_service_ready = False
        self.turtle_spawned = False
        self.turtle_pose_cansubscribe = False

        self.timer = self.create_timer(1.0, self.on_timer)

    def on_timer(self):
        if self.turtle_spawning_service_ready:
            if self.turtle_spawned:
                self.turtle_pose_cansubscribe = True
            else:
                if self.result.done():
                    self.get_logger().info(
                        f'Successfully spawned {self.result.result().name}')
                    self.turtle_spawned = True
                else:
                    self.get_logger().info('Spawn is not finished')
        else:
            if self.spawner.service_is_ready():
                request = Spawn.Request()
                request.name = 'turtle3'
                request.x = float(4)
                request.y = float(2)
                request.theta = float(0)
                self.result = self.spawner.call_async(request)
                self.turtle_spawning_service_ready = True
            else:
                self.get_logger().info('Service is not ready')

        if self.turtle_pose_cansubscribe:
            self.vel_pub = self.create_publisher(Twist, 'turtle3/cmd_vel', 10)
            self.sub = self.create_subscription(Pose, 'turtle3/pose', self.handle_turtle_pose, 10)
            self.pub = self.create_publisher(PointStamped, 'turtle3/turtle_point_stamped', 10)

    def handle_turtle_pose(self, msg):
        vel_msg = Twist()
        vel_msg.linear.x = 1.0
        vel_msg.angular.z = 1.0
        self.vel_pub.publish(vel_msg)

        ps = PointStamped()
        ps.header.stamp = self.get_clock().now().to_msg()
        ps.header.frame_id = 'world'
        ps.point.x = msg.x
        ps.point.y = msg.y
        ps.point.z = 0.0
        self.pub.publish(ps)


def main():
    rclpy.init()
    node = PointPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()
