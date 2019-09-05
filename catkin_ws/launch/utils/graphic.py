import numpy as np
from open3d import *
from time import sleep    

def main():
    pcd = read_point_cloud("1567176978378136.pcd") # Read the point cloud
    
    draw_geometries([pcd]) # Visualize the point cloud     

if __name__ == "__main__":
    main()