import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from vision_msgs.msg import Detection2DArray, Detection2D, BoundingBox2D, ObjectHypothesis
from std_msgs.msg import Header
import cv2 # For dummy image processing demonstration
import numpy as np # For dummy image data
import time

class IsaacROSDummyObjectDetector(Node):

    def __init__(self):
        super().__init__('isaac_ros_dummy_object_detector')
        self.image_subscriber_ = self.create_subscription(
            Image,
            'camera/image_raw',
            self.image_callback,
            10)
        self.detection_publisher_ = self.create_publisher(Detection2DArray, 'object_detections', 10)
        self.get_logger().info('IsaacROSDummyObjectDetector node has started, subscribing to /camera/image_raw.')
        self.get_logger().info('Publishing dummy detections to /object_detections.')

        # Dummy image for demonstration if no actual camera is publishing
        self.dummy_image_timer = self.create_timer(1.0, self.publish_dummy_image) # Publish dummy image every 1 second
        self.width = 640
        self.height = 480

    def publish_dummy_image(self):
        dummy_img = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        cv2.putText(dummy_img, f'Time: {time.time():.1f}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # Convert numpy array to ROS Image message
        img_msg = Image()
        img_msg.header = Header(stamp=self.get_clock().now().to_msg(), frame_id='camera_link')
        img_msg.height = dummy_img.shape[0]
        img_msg.width = dummy_img.shape[1]
        img_msg.encoding = 'rgb8'
        img_msg.is_bigendian = 0
        img_msg.step = dummy_img.shape[1] * dummy_img.shape[2] # (width * channels)
        img_msg.data = dummy_img.tobytes()

        # self.get_logger().debug('Published dummy image.')
        # In a real scenario, this would come from a camera driver
        # We're publishing it here for self-contained example.
        # self.image_publisher_.publish(img_msg) # If we were a publisher as well

        # Directly call the image_callback for demonstration without a full ROS 2 setup
        # In a real scenario, the callback would be triggered by the subscription
        self.image_callback(img_msg)


    def image_callback(self, msg):
        self.get_logger().debug('Received image. Simulating object detection.')

        detection_array_msg = Detection2DArray()
        detection_array_msg.header = msg.header # Use the same header as the incoming image

        # Simulate detecting two objects: a 'robot' and a 'target'
        # In a real Isaac ROS pipeline, this would be the output of a deep learning model

        # Detection 1: Robot
        detection1 = Detection2D()
        detection1.header = msg.header
        detection1.bbox = BoundingBox2D()
        detection1.bbox.center.x = float(msg.width) * 0.25 # Center X
        detection1.bbox.center.y = float(msg.height) * 0.50 # Center Y
        detection1.bbox.size_x = float(msg.width) * 0.1 # Width
        detection1.bbox.size_y = float(msg.height) * 0.2 # Height

        hypothesis1 = ObjectHypothesis()
        hypothesis1.class_id = 'robot'
        hypothesis1.score = 0.95
        detection1.results.append(hypothesis1)
        detection_array_msg.detections.append(detection1)

        # Detection 2: Target
        detection2 = Detection2D()
        detection2.header = msg.header
        detection2.bbox = BoundingBox2D()
        detection2.bbox.center.x = float(msg.width) * 0.75 # Center X
        detection2.bbox.center.y = float(msg.height) * 0.40 # Center Y
        detection2.bbox.size_x = float(msg.width) * 0.15 # Width
        detection2.bbox.size_y = float(msg.height) * 0.15 # Height

        hypothesis2 = ObjectHypothesis()
        hypothesis2.class_id = 'target'
        hypothesis2.score = 0.88
        detection2.results.append(hypothesis2)
        detection_array_msg.detections.append(detection2)

        self.detection_publisher_.publish(detection_array_msg)
        self.get_logger().info(f'Published {len(detection_array_msg.detections)} dummy object detections.')


def main(args=None):
    rclpy.init(args=args)
    isaac_ros_dummy_object_detector = IsaacROSDummyObjectDetector()
    rclpy.spin(isaac_ros_dummy_object_detector)
    isaac_ros_dummy_object_detector.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()