import rospy
import os
import subprocess
from _thread import start_new_thread
from time import sleep
start_new_thread(os.system,("roslaunch realsense2_camera rs_camera.launch align_depth:=true enable_infra1:=false enable_infra2:=false > /dev/null 2>&1",))
start_new_thread(os.system,('roslaunch rtabmap_ros rtabmap.launch rtabmap_args:="--delete_db_on_start" depth_topic:=/camera/aligned_depth_to_color/image_raw rgb_topic:=/camera/color/image_raw camera_info_topic:=/camera/color/camera_info approx_sync:=false > /dev/null 2>&1',))
# sleep(10)
# start_new_thread(os.system,('rosservice call /rtabmap/pause',))
# start_new_thread(os.system,('rosservice call /rtabmap/publish_map 1 1 0',))
# start_new_thread(os.system,('rosrun pcl_ros pointcloud_to_pcd input:=/rtabmap/cloud_map',))
exit()