import images
from _thread import start_new_thread
from filter import get_diff
import cv2
json=[]
points=0


def update_graph():
    global json,points
    while True:
        if abs(images.position['z'])>(points+1)/10.0:
            color=images.image['color']
            depth=images.image['depth']
            diff =get_diff(color,depth)
            if diff is not None:
                temp={}
                temp['y']=round(diff, 3)
                temp['x']=round(abs(images.position['z']), 3)
                json.append(temp)
                points+=1

def reset_globals():
    global json , points
    json=[]
    points=0

start_new_thread(update_graph,(),)


# while True:
#     color=images.image['color']
#     depth=images.image['depth']
#     if color is not None:
#         diff =get_diff(color,depth)
#         if diff is not None:
#             print diff
        



