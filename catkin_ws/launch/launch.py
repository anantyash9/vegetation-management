import roslaunch
import rospy
import signal
import sys
def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        stop_nodes()
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


rospy.init_node('launcher', anonymous=True)
uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)
realsense = roslaunch.parent.ROSLaunchParent(uuid, ["rs_camera.launch"])
rtabmap = roslaunch.parent.ROSLaunchParent(uuid, ["map_make.launch"])
websockets= roslaunch.parent.ROSLaunchParent(uuid, ["rosbridge_websocket.launch"])
def start_nodes():
    realsense.start()
    rtabmap.start()
    websockets.start()


def stop_nodes():
    rtabmap.shutdown()
    realsense.shutdown()
    websockets.shutdown()

start_nodes()
while True:
    pass