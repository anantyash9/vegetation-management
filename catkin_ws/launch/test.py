import images
import pose
import rospy
from _thread import start_new_thread

import cv2
color = images.color()
while True:
    if color.image is not None:
        cv2.imshow("Image window", color.image)
        cv2.imwrite("color.jpeg",color.image)
        cv2.waitKey(3)
# p = pose.pose()
# while True:
#     print(p.position)