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
from utils import *

FILE = Path(__file__).absolute()
sys.path.append(FILE.parents[0].as_posix())



class Car_SP(rclpy.node.Node):
    def __init__(self):
        super().__init__('param_vel_node')
        self.msg = Twist()
        self.bridge = CvBridge()

        self.publisher = self.create_publisher(Twist, '/skidbot/cmd_vel', 10)

        # take twist sub
        self.controlsub = self.create_subscription(
            Twist,
            '/skidbot/cmd_vel',
            self.control_callback,10)
        self.controlsub

        param_descriptor = ParameterDescriptor(
            description='Sets the velocity (in m/s) of the robot.')
        self.declare_parameter('velocity', 0.0, param_descriptor)
        
        # make camerasub __init__
        self.camsub = self.create_subscription(
            Image,
            'skidbot/camera_sensor/image_raw',
            self.camera_callback,
            10)

        self.camsub     
        self.vlz = 0.0         
        self.speed = 0.0   
        
                                                                                                                                                        
    def camera_callback(self, data): # Remember, image in gazebo output with 30 image in 1s
        # convert image to cv2
        img = self.bridge.imgmsg_to_cv2(data, "bgr8")
        ## always resize image before reshape
        img = cv2.resize(img,(120,160), interpolation = cv2.INTER_AREA)
        # print("here:  " + str(img.shape))
        # save and export image to log.csv
        test = Utils(image=img,data=[self.vlz,self.speed])
        test.export_to_csv()


    def control_callback(self,msg):
        
        self.vlz =  msg.angular.z
        self.speed = msg.linear.x


def main():
    rclpy.init()
    node = Car_SP()
    rclpy.spin(node)


if __name__ == '__main__':
    main()