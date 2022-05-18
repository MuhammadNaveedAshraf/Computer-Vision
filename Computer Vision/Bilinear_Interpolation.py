# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 14:55:06 2020

@author: emnas
"""
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

image=cv.imread('image 1.jpg',0)
def Bilinear_Interpolation(image,new_height,new_width):
    height,width=image.shape
    resized_image=np.zeros((new_height,new_width))
    #ratio to map indexes to new size
    if new_height>1:
        ratio_y=(height-1)/(new_height-1)
    if new_width>1:
        ratio_x=(width-1)/(new_width-1)
    
    for i in range(0,new_height):
        for j in range(0,new_width):
            
            #Algorithm
            #X=A(1-wx)+Bwx
            #Y=C (1-wx)+Dwx
            
            #Z=X(1-wy)+Ywy
            #replacing X and Y
            #Z=(A(1-wx)+Bwx)(1-wy) + (C(1-wx)+Dwx)wy
            #Z=A(1-wx)(1-wy) + Bwx(1-wy) + C(1-wx)wy + Dwxwy
            
            # getting distances for neighbours
            lower_x=np.floor(ratio_x*j).astype(np.int32)
            lower_y=np.floor(ratio_y*i).astype(np.int32)
            higher_x=np.ceil(ratio_x*j).astype(np.int32)
            higher_y=np.ceil(ratio_y*i).astype(np.int32)
            #getting neighbours
            if(higher_x<width and higher_y<height):
                A=image[lower_y,lower_x]
                B=image[lower_y,higher_x]
                C=image[higher_y,lower_x]
                D=image[higher_y,higher_x]
            
            #getting weightage(distance from neighbour)
            wx= ((ratio_x*j)-lower_x)
            #(1-wx)
            wy= ((ratio_y*i)-lower_y)
            #(1-wy)
            
            #applying weightage to generate index value
            resized_image[i,j]= A*(1-wx)*(1-wy) + B*wx*(1-wy) + C*wy*(1-wx) + D*wx*wy
    resized_image=resized_image.astype(np.uint8)        
    return resized_image
# resized_image=Bilinear_Interpolation(image,720,720)
# plt.imshow(image, cmap='gray')
# plt.show()
# plt.close()        

# plt.imshow(resized_image, cmap='gray')
# plt.show()
# plt.close()
