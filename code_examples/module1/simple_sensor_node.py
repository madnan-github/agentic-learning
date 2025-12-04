import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from std_msgs.msg import String
import math
import time

class SimpleSensorPublisher(Node):

    def __init__(self):
        super().__init__('simple_sensor_publisher')
        self.imu_publisher_ = self.create_publisher(Imu, 'imu/data', 10)
        self.string_publisher_ = self.create_publisher(String, 'sensor/status', 10)
        self.timer = self.create_timer(0.1, self.publish_sensor_data) # 10 Hz
        self.i = 0

        self.get_logger().info('SimpleSensorPublisher node has started.')

    def publish_sensor_data(self):
        # Publish dummy IMU data
        imu_msg = Imu()
        imu_msg.header.stamp = self.get_clock().now().to_msg()
        imu_msg.header.frame_id = 'imu_link'

        # Simulate a slow rotation around Z-axis
        angle = self.i * 0.01
        imu_msg.orientation.w = math.cos(angle / 2.0)
        imu_msg.orientation.z = math.sin(angle / 2.0)

        imu_msg.angular_velocity.z = 0.1 # Constant rotation velocity
        imu_msg.linear_acceleration.x = 0.1 # Constant acceleration

        self.imu_publisher_.publish(imu_msg)
        self.get_logger().debug(f'Published IMU data: {imu_msg.orientation.z:.2f}')

        # Publish a simple status string
        string_msg = String()
        string_msg.data = f'Sensor operating normally. Cycle: {self.i}'
        self.string_publisher_.publish(string_msg)
        self.get_logger().debug(f'Published status: {string_msg.data}')

        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    simple_sensor_publisher = SimpleSensorPublisher()
    rclpy.spin(simple_sensor_publisher)
    simple_sensor_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
