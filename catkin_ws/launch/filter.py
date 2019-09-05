import cv2 
import numpy as np 
  
def appy_filter(frame,typ):
    # It converts the BGR color space of image to HSV color space 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
      
    if typ=='Blue':

        lower = np.array([100, 150, 150]) 
        upper = np.array([130,255, 255])
    else:
        lower = np.array([40, 20, 150]) 
        upper = np.array([75,255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    
    return mask

def region_of_interest(img, vertices):
    """
    Applies an image mask.
    
    Only keeps the region of the image defined by the polygon
    formed from `vertices`. The rest of the image is set to black.
    """
    #defining a blank mask to start with
    mask = np.zeros_like(img)   
    
    #defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(img.shape) > 2:
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
        
    #filling pixels inside the polygon defined by "vertices" with the fill color    
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    
    #returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def get_diff(color,depth):
    # imshape = color.shape
    # vertices = np.array([[(0,imshape[0]//(3.0/2.0)),(0,(imshape[0]//3.0)), ((imshape[1]),(imshape[0]//3.0)), (imshape[1],imshape[0]//(3.0/2.0))]], dtype=np.int32)
    # color = region_of_interest(color,vertices)
    # depth = region_of_interest(depth,vertices)
    green=appy_filter(color,'Green')
    blue=appy_filter(color,'Blue')
    # cv2.imshow('green',green)
    # cv2.imshow('blue',blue)
    # cv2.waitKey(3)
    blue_no=0
    green_no=0
    Val=None
    green_depth = cv2.bitwise_and(depth, depth, mask = green)
    blue_depth = cv2.bitwise_and(depth, depth, mask = blue)
    try:
        blue_depth_min=blue_depth[np.nonzero(blue_depth)].min()
        green_depth_min=green_depth[np.nonzero(green_depth)].min()
        Val=(green_depth_min-blue_depth_min)*0.0010000000474974513
        if Val >5:
            Val=None

    except ValueError:
        pass
    return Val




