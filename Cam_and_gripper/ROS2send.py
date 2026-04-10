#ros2 pkg create --build-type ament_python photosphere_publisher
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class PhotospherePublisher(Node):
    def __init__(self):
        super().__init__('photosphere_publisher')
        self.publisher_ = self.create_publisher(Image, 'photosphere', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.bridge = CvBridge()
        self.photosphere_path = 'path/to/your/photosphere.jpg'

    def timer_callback(self):
        img = cv2.imread(self.photosphere_path)
        msg = self.bridge.cv2_to_imgmsg(img, encoding='bgr8')
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing photosphere')

def main(args=None):
    rclpy.init(args=args)
    node = PhotospherePublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
#terminal
#colcon build
#source install/setup.bash
#ros2 run photosphere_publisher photosphere_publisher
#ros2 topic echo /photosphere