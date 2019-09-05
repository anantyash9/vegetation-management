#!/usr/bin/env python
from __future__ import print_function

import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image,PointCloud2
from cv_bridge import CvBridge, CvBridgeError
from _thread import start_new_thread
import numpy as np
import utils
from nav_msgs.msg import Odometry
from filter import appy_filter

image={'color':None,'depth':None}
position={'x':0,'y':0,'z':0}
point=None
bridge = CvBridge()

class pose_mapper:

  def __init__(self,topic):
    self.sub = rospy.Subscriber(topic,Odometry,self.callback)

  def callback(self,msg):
    global position
    position['x'] =msg.pose.pose.position.x
    position['y'] =msg.pose.pose.position.y
    position['z'] =msg.pose.pose.position.z

class pointcloud:

  def __init__(self,topic):
    self.sub = rospy.Subscriber(topic,PointCloud2,self.callback)

  def callback(self,msg):
    global point
    point=bytes(msg)



class image_converter:

  def __init__(self,topic,typ):
    self.image_sub = rospy.Subscriber(topic,Image,self.callback)
    self.type = typ
    self.image=None
  def callback(self,data):
    global image
    try:
        if self.type =='color': 
            cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
        else:
            cv_image = bridge.imgmsg_to_cv2(data, "16UC1")

    except CvBridgeError as e:
        print(e)
    image[self.type]=cv_image
def color():
  color = image_converter("/camera/color/image_raw",'color')
  return color
def depth():
  depth = image_converter("/camera/aligned_depth_to_color/image_raw",'depth')
  return depth
   
def node():
  rospy.init_node(name='velo',anonymous=True, disable_signals=True)
  pose_listner = pose_mapper('/rtabmap/odom')
  color = image_converter("/camera/color/image_raw",'color')
  depth = image_converter("/camera/aligned_depth_to_color/image_raw",'depth')
  point_listner = pointcloud('/rtabmap/cloud_map')
  rospy.spin()
  
start_new_thread(node,(),)
# while True:
#     if image['depth'] is not None:
#         depth=image['depth']
#         d=depth[240,320]*0.0010000000474974513
#         print (d)
#         utils.reset_globals()
#         edges = utils.process_static_image(cv2.convertScaleAbs(depth, alpha=0.3),image['color'])
#         blur = cv2.GaussianBlur(image['depth'],(3,3),0)
#         # median = cv2.medianBlur(img,5)
#         # blur = cv2.bilateralFilter(img,9,75,75)
#         img = cv2.applyColorMap(cv2.convertScaleAbs(blur, alpha=0.3), cv2.COLORMAP_JET)
#         cv2.circle(img, (320,240), 5, 5)
#         cv2.imshow("Image window",edges )
#         cv2.waitKey(3)


# while True:
#     if image['color'] is not None:
#         color=image['color']
#         img=appy_filter(color,'Blue')
#         cv2.imshow("Blue",img )
#         result = cv2.bitwise_and(image['depth'], image['depth'], mask = img)
#         blue=0
#         green=0
#         try:
#           blue=result[np.nonzero(result)].min()
#         except ValueError:
#           pass
#         img=appy_filter(color,'Green')  
#         result = cv2.bitwise_and(image['depth'], image['depth'], mask = img)
#         try:
#           green=result[np.nonzero(result)].min()
#         except ValueError:
#           pass
#         if blue !=0 and green !=0:
#           diff=(green-blue)*0.0010000000474974513
#           print(diff)
#         #cv2.imwrite('color.jpg',color)
#         cv2.imshow("Image window",img )
#         cv2.waitKey(3)