# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:43:55 2020

@author: emnas
"""
from FiltersOnly import ApplyFilter
from FiltersOnly import normalize
from FiltersOnly import gaussianFilter
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

prewitt1=np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
prewitt2=np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

sobel_vertical=np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
sobel_horizontal=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])

laplacian_filter=np.array([[0,1,0],[1,-4,1],[0,1,0]])
laplacian_filter1=np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
laplacian_filter2=np.array([[1,1,1],[1,-8,1],[1,1,1]])
laplacian_filter3=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
def magnitude(img,hori_filter,vert_filter):
    vertical_edge=ApplyFilter(img, vert_filter)
    horizontal_edge=ApplyFilter(img, hori_filter)
    new_img=np.sqrt(np.square(vertical_edge)+np.square(horizontal_edge))
    new_img=normalize(new_img)
    return new_img

# image=cv.imread('canny_practice.png',0)
# new_img_prewitt=magnitude(image,prewitt2,prewitt1)
# plt.imshow(new_img_prewitt,cmap='gray')
# plt.show()
# plt.close()
# new_img_sobel=magnitude(image,sobel_horizontal,sobel_vertical)
# plt.imshow(new_img_sobel,cmap='gray')
# plt.show()
# plt.close()
# image1=ApplyFilter(image,gaussianFilter(3,1))
# image1=ApplyFilter(image1,laplacian_filter)
# image1=normalize(image1)
# image2=ApplyFilter(image,gaussianFilter(3,1))
# image2=ApplyFilter(image2,laplacian_filter1)
# image2=normalize(image2)
# image3=ApplyFilter(image,gaussianFilter(3,1))
# image3=ApplyFilter(image3,laplacian_filter2)
# image3=normalize(image3)
# image4=ApplyFilter(image,gaussianFilter(3,1))
# image4=ApplyFilter(image4,laplacian_filter3)
# image4=normalize(image4)
# # new_img2=magnitude(image,laplacian_filter1,laplacian_filter1)
# plt.imshow(image1,cmap='gray')
# plt.show()
# plt.close()
# cv.imshow('Laplacian1', image1)
# cv.imshow('Laplacian2', image2)
# cv.imshow('Laplacian3', image3)
# cv.imshow('Laplacian4', image4)
# cv.imshow('prewitt', new_img_prewitt)
# cv.imshow('sobel', new_img_sobel)
# cv.waitKey(0)
# cv.destroyAllWindows()