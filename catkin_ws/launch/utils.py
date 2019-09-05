import math
import numpy as np
import cv2


#Global variables
"These variables are used to store the x and y co-ordinates of the last 5 frames." 
glbx =[]
gyb =0
gltx =[]
gyt =0
grbx =[]
grtx =[]


def reset_globals():
    "Resets the global variables"
    global glbx, gyb, gltx, gyt, grbx, grtx
    glbx =[]
    gyb =0
    gltx =[]
    gyt =0
    grbx =[]
    grtx =[]
    
def grayscale(img):
    "Applies the Grayscale transform"
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    
def hls(img):
    "convert the image to HSL (Hue, Saturation, Lightness) space"
    return cv2.cvtColor(img, cv2.COLOR_RGB2HLS)

def lane_pass_filter(img):
    "filters out everything(mostly) that is not white or yellow "
    hls_image = hls(img)
    l_thresh = np.uint8([  0, 200,   0])
    u_thresh = np.uint8([255, 255, 255])
    white_pass = cv2.inRange(hls_image, l_thresh, u_thresh)
    l_thresh = np.uint8([ 12,   0, 100])
    u_thresh = np.uint8([ 45, 255, 255])
    yellow_pass = cv2.inRange(hls_image, l_thresh, u_thresh)
    yellow_white_pass = cv2.bitwise_or(white_pass, yellow_pass)
    return cv2.bitwise_and(img, img, mask = yellow_white_pass)
    
def canny(img, low_threshold, high_threshold):
    """Applies the Canny transform"""
    return cv2.Canny(img, low_threshold, high_threshold)

def gaussian_blur(img, kernel_size):
    """Applies a Gaussian Noise kernel"""
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

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

def draw_lines(img, lines,end_point, color=[255, 0, 0], thickness=10):
    imshape = img.shape
    # only use this if there are lines to begin with else use running average from last 5 frames
    if lines !=None:
        filtered=[]
        filtered = filter(lambda x: abs(x[3]-x[1])<10, lines[0])
        if len(filtered)>0:
            slopes=[(x[3]-x[1])*1.0/(x[2]-x[0]*1.0) for x in filtered]
            # find the average slope for left and right lane
            slope = float(sum(slopes)) / len(slopes)*1.0
            
            # find average x and y position for each lane
            x = int(sum([x[0]+x[2] for x in filtered]) / len(filtered))
            y = int(sum([y[1]+y[3] for y in filtered]) / len(filtered))
            # The endpoints for the extrapolated line 
            xe =imshape[1]
            xs =0
            # The 'c' in y=mx+c 
            c = y-(slope*x)
            # Find the top and bottom points using the calculated 'c'.
            ye= int(xe*slope+c)
            ys= int(xs*slope+c)
                           
            cv2.line(img, (xs,ys),(xe,ye), color, thickness)
 
def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap,end_point):

    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines,end_point)
    return line_img

# Python 3 has support for cool math symbols.

def weighted_img(img, initial_img, a=0.8, b=1., y=0.):

    return cv2.addWeighted(initial_img, a, img, b, y)

def process_static_image(image,color):
    " Draw lanes on images"
    # filter out everything but the lanes
    blur_gray = gaussian_blur(image,3)
    # edge dectection
    edges = canny(image,240,255)
    # create a mask for region of interest
    imshape = image.shape
    vertices = np.array([[(0,imshape[0]//(3.0/2.0)),(0,(imshape[0]//3.0)), ((imshape[1]),(imshape[0]//3.0)), (imshape[1],imshape[0]//(3.0/2.0))]], dtype=np.int32)
    masked_image = region_of_interest(edges,vertices)
    rho = 2 # distance resolution in pixels of the Hough grid
    theta = np.pi/180 # angular resolution in radians of the Hough grid
    threshold = 10     # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 100 #minimum number of pixels making up a line
    max_line_gap = 30    # maximum gap in pixels between connectable line segments
    region_end_point = imshape[0]//(3.0/2.0) # the topmost point to which lane lines will be drawn
    transformed_img = hough_lines(masked_image, rho, theta, threshold, min_line_length, max_line_gap,region_end_point)
    weighted = weighted_img(transformed_img,color)
    
    return weighted