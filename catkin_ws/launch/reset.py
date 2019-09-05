import os
from _thread import start_new_thread
# def start_pointcloud():
#     start_new_thread(os.system,("roslaunch realsense2_camera rs_camera.launch align_depth:=true enable_infra1:=false enable_infra2:=false > /dev/null 2>&1",))
#     sleep(1)
#     start_new_thread(os.system,("roslaunch map_make.launch > /dev/null 2>&1",))
#     sleep(1)
#     start_new_thread(os.system,("roslaunch rosbridge_server rosbridge_websocket.launch > /dev/null 2>&1",))
#     sleep(1)
#     start_new_thread(os.system,("rosrun tf2_web_republisher tf2_web_republisher > /dev/null 2>&1",))

def reset():
    os.system("rosservice call rtabmap/reset_odom")
    os.system("rosservice call rtabmap/reset")

def save():
    os.system("rosservice call rtabmap/pause")
    start_new_thread(os.system,("rosrun pcl_ros pointcloud_to_pcd input:=/rtabmap/cloud_map",),)
    os.system("rosservice call rtabmap/publish_map")
    os.system("rosservice call rtabmap/resume")

