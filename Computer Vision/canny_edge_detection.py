# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:52:12 2020

@author: emnas
"""
from FiltersOnly import ApplyFilter
from FiltersOnly import normalize
from FiltersOnly import gaussianFilter
import numpy as np
import cv2 as cv
import math
import matplotlib.pyplot as plt
import argparse

sobel_horizontal=np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
sobel_vertical=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])

def magnitude(img,vert_filter,hori_filter):
    vertical_edge=ApplyFilter(img, vert_filter)
    horizontal_edge=ApplyFilter(img, hori_filter)
    new_img=np.zeros(vertical_edge.shape)
    new_img=np.sqrt(np.square(vertical_edge)+np.square(horizontal_edge))
    angles=np.arctan2(vertical_edge, horizontal_edge)
    new_img=normalize(new_img)
    return new_img,angles

def non_max_suppression(img, D):
    M, N = img.shape
    Z = np.zeros((M,N), dtype=np.int32)
    angle = D * 180. / np.pi
    angle[angle < 0] += 180
    
    for i in range(1,M-1):
        for j in range(1,N-1):
            try:
                q = 225
                r = 255
                
               #angle 0
                if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                    q = img[i, j+1]
                    r = img[i, j-1]
                #angle 45
                elif (22.5 <= angle[i,j] < 67.5):
                    q = img[i+1, j-1]
                    r = img[i-1, j+1]
                #angle 90
                elif (67.5 <= angle[i,j] < 112.5):
                    q = img[i+1, j]
                    r = img[i-1, j]
                #angle 135
                elif (112.5 <= angle[i,j] < 157.5):
                    q = img[i-1, j-1]
                    r = img[i+1, j+1]

                if (img[i,j] >= q) and (img[i,j] >= r):
                    Z[i,j] = img[i,j]
                else:
                    Z[i,j] = 0

            except IndexError as e:
                pass
    
    return Z
def threshold(img, lowThresholdRatio=0.05, highThresholdRatio=0.10):
    
    highThreshold = img.max() * highThresholdRatio;
    lowThreshold = highThreshold * lowThresholdRatio;
    
    M, N = img.shape
    res = np.zeros((M,N))
    
    weak = np.int32(85)
    strong = np.int32(255)
    
    strong_i, strong_j = np.where(img >= highThreshold)
    zeros_i, zeros_j = np.where(img < lowThreshold)
    
    weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))
    
    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak
    res=res.astype(np.uint8)
    return res
def hysteresis(img, weak, strong=255):
    M,N = img.shape
    for i in range(1, M-1):
        for j in range(1, N-1):
            if (img[i,j] == weak):
                try:
                    if ((img[i+1, j-1] == strong) or (img[i+1, j] == strong) or (img[i+1, j+1] == strong)
                        or (img[i, j-1] == strong) or (img[i, j+1] == strong)
                        or (img[i-1, j-1] == strong) or (img[i-1, j] == strong) or (img[i-1, j+1] == strong)):
                        img[i, j] = strong
                    else:
                        img[i, j] = 0
                except IndexError as e:
                    pass
    return img
image=cv.imread('canny_practice.png',0)
image1=ApplyFilter(image,gaussianFilter(7,1))    #step # 1

# sobelx = cv.Sobel(image,cv.CV_64F,1,0,ksize=3)
# sobely = cv.Sobel(image,cv.CV_64F,0,1,ksize=3)
# new_img3=(np.sqrt(np.square(sobelx)+np.square(sobely)))
# angles2=np.arctan2(sobely,sobelx)
new_img1,angles=magnitude(image1,sobel_vertical,sobel_horizontal) #step # 2    
image1=normalize(image1)

#new_img=normalize(new_img1)
plt.imshow(new_img1,cmap='gray')
plt.show()
plt.close()
new_img2=non_max_suppression(new_img1,angles ) #step # 3
plt.imshow(new_img2,cmap='gray')
plt.show()
plt.close()
new_img2=threshold(new_img2)    #step # 4
plt.imshow(new_img2,cmap='gray')
plt.show()
plt.close()
new_img2=hysteresis(new_img2, 85) #step # 5
new_img1=normalize(new_img1)
plt.imshow(new_img2,cmap='gray')
plt.show()
plt.close()
cv.imshow('original', image)
cv.imshow('gaussian blur', image1)
#cv.imshow('sobel before', new_img1)
cv.imshow('sobel before', new_img1)
cv.imshow('sobel after', new_img2)
cv.waitKey(0)
cv.destroyAllWindows()
