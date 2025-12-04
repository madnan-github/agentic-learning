---
title: Basic Sensor Integration
description: Learn about integrating common robot sensors with ROS 2, including reading sensor data and understanding ROS 2 sensor message types.
slug: /module1/chapter2/lesson2-sensor-integration
sidebar_label: Sensor Integration
---

# Basic Sensor Integration

Robots interact with their environment through sensors. Integrating these sensors with ROS 2 is crucial for building intelligent and autonomous systems. This lesson will introduce you to common sensor types, how their data is represented in ROS 2 messages, and how to read this data in your ROS 2 applications.

## 1. Common Robot Sensor Types

Robots utilize a variety of sensors to perceive their surroundings:

-   **Inertial Measurement Units (IMUs)**: Provide data on orientation, angular velocity, and linear acceleration. Essential for robot localization and stability.
-   **Lidar/Depth Cameras**: Generate 3D point clouds or depth images, used for mapping, navigation, and object detection.
-   **RGB Cameras**: Capture visual information, critical for computer vision tasks.
-   **Ultrasonic/Infrared Sensors**: Used for short-range distance measurement and obstacle detection.
-   **Encoders**: Measure joint positions and velocities, providing feedback for motor control.

## 2. ROS 2 Sensor Message Types

ROS 2 provides a rich set of standard message types (`sensor_msgs`) to represent data from various sensors:

-   `sensor_msgs/Imu`: For IMU data (orientation, angular velocity, linear acceleration).
-   `sensor_msgs/LaserScan`: For 2D laser range finders (Lidar).
-   `sensor_msgs/PointCloud2`: For 3D point cloud data (from Lidar or depth cameras).
-   `sensor_msgs/Image`: For camera images.
-   `sensor_msgs/JointState`: For joint positions, velocities, and efforts (often from encoders).

Each message type includes a `std_msgs/Header` which contains a `timestamp` (when the data was recorded) and a `frame_id` (the coordinate frame the data refers to).

## 3. Reading Sensor Data in ROS 2

Reading sensor data typically involves subscribing to a ROS 2 topic where a sensor driver node is publishing the data.

### Example: Subscribing to an IMU Topic

Let's say you have a simulated IMU sensor publishing data on the `/imu/data` topic. You can create a ROS 2 Python subscriber to read this data:

```python
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu

class ImuSubscriber(Node):

    def __init__(self):
        super().__init__('imu_subscriber')
        self.subscription = self.create_subscription(
            Imu,
            '/imu/data',
            self.imu_callback,
            10)
        self.subscription  # prevent unused variable warning

    def imu_callback(self, msg):
        self.get_logger().info(
            f'IMU Data: \n'
            f'  Orientation (x,y,z,w): ({msg.orientation.x:.2f}, {msg.orientation.y:.2f}, {msg.orientation.z:.2f}, {msg.orientation.w:.2f})\n'
            f'  Angular Velocity (x,y,z): ({msg.angular_velocity.x:.2f}, {msg.angular_velocity.y:.2f}, {msg.angular_velocity.z:.2f})\n'
            f'  Linear Acceleration (x,y,z): ({msg.linear_acceleration.x:.2f}, {msg.linear_acceleration.y:.2f}, {msg.linear_acceleration.z:.2f})'
        )

def main(args=None):
    rclpy.init(args=args)
    imu_subscriber = ImuSubscriber()
    rclpy.spin(imu_subscriber)
    imu_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

This node subscribes to `sensor_msgs/Imu` messages and prints the orientation, angular velocity, and linear acceleration data. In a real application, you would process this data for navigation, control, or other robotic tasks.

## 4. Coordinate Frames and TF

Sensor data is always associated with a **coordinate frame** (specified by `frame_id` in the message header). The **TF (Transform) tree** in ROS 2 manages the relationships between different coordinate frames in a robot system. Understanding TF is crucial for correctly interpreting sensor data from various parts of your robot.

For example, an IMU might report data in its own sensor frame, which then needs to be transformed to the robot's base frame for consistent use in navigation algorithms.

## 5. Next Steps

In the final lesson of this module, we will create a simple simulated sensor node that publishes data, allowing you to practice subscribing to and reading this data.
