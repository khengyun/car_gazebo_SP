import rclpy
import rclpy.node
from rcl_interfaces.msg import ParameterDescriptor
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image, CompressedImage
import csv
import time
from typing import Tuple, Union
from email.mime import image
from fileinput import filename
import os, sys
import rclpy
from rclpy.node import Node
from keras.models import load_model
from sensor_msgs.msg import Image, CompressedImage
import cv2
import numpy as np
import time
from pathlib import Path
import torch
import torch.backends.cudnn as cudnn
from keras.models import load_model
import os, sys
import time
from pathlib import Path
from rich import print
FILE = Path(__file__).absolute()
sys.path.append(FILE.parents[0].as_posix())
# from sensor_msgs.msg import Image, CompressedImage



class Car_SP(rclpy.node.Node):
    def __init__(self):
        super().__init__('param_vel_node')
        self.timer = self.create_timer(0.1, self.timer_callback)

        # make mgspub
        self.publisher = self.create_publisher(Twist, '/skidbot/cmd_vel', 10)
        self.msg = Twist()
        self.bridge = CvBridge()
        param_descriptor = ParameterDescriptor(
            description='Sets the velocity (in m/s) of the robot.')
        self.declare_parameter('velocity', 0.0, param_descriptor)

        
        # init linez
        self.linez = 0.0
  
        # make camerasub __init__
        self.subscription = self.create_subscription(
            Image,
            'skidbot/camera_sensor/image_raw',
            self.camera_callback,
            10)
        self.subscription            
        self.vlz = 0            
                                                                                                                                                        
    def camera_callback(self, data):
        t0 = time.time()
        img = self.bridge.imgmsg_to_cv2(data, "bgr8")

        ## always resize image before reshape
        img = cv2.resize(img,(120,160), interpolation = cv2.INTER_AREA)
        
        print("here:  "+str(img.shape))
        model = load_model('model.h5')
        img = img.reshape((1,) + (120,160,3))

        result = model.predict(img)
        print(np.float32(result[0])[0][0])

        self.vlz = np.float32(result[0])[0][0]

    def timer_callback(self):

        self.msg.linear.x = 0.235
        # self.publisher.publish(self.msg)
        # vel
        self.msg.angular.z = float(self.vlz)
        # self.linez+=1
        # self.msg.angular.z = 1.0
        self.publisher.publish(self.msg)

def main():
    rclpy.init()
    node = Car_SP()
    rclpy.spin(node)


if __name__ == '__main__':
    main()