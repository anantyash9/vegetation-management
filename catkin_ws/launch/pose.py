import roslib
import rospy
from nav_msgs.msg import Odometry
from _thread import start_new_thread

position={'x':0,'y':0,'z':0}

class pose_mapper:

  def __init__(self,topic):
    self.sub = rospy.Subscriber(topic,Odometry,self.callback)

  def callback(self,msg):
    position['x'] =msg.pose.pose.position.x
    position['y'] =msg.pose.pose.position.y
    position['z'] =msg.pose.pose.position.z

def node():
  rospy.init_node(name='pose',anonymous=True, disable_signals=True)
  pose_listner = pose_mapper('/rtabmap/odom')
  rospy.spin()

start_new_thread(node,(),)

