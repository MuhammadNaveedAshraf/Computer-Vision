# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:41:01 2020

@author: emnas
"""
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def oneStep(portion,fltr):
    z=np.multiply(portion,fltr)
    return z.sum()
def pad(filterSize):
    p=(filterSize-1)/2
    return p
def applyPad0(pad,image):
    x,y=image.shape
    x=int(x+(2*pad))
    y=int(y+(2*pad))
    img=np.zeros((x,y))
    img[pad:x-pad,pad:y-pad]=image
    return img
def ApplyFilter(image,filter1):
    x=image.shape[0]
    y=image.shape[1]
    f=filter1.shape[0]
    p=int(pad(filter1.shape[0]))
    new_img=applyPad0(p,image)

    x=x+2*p-f+1
    y=y+2*p-f+1

    output_img=np.zeros((x,y))
    filter1=rotateFilter(filter1)
    for x in range(0,output_img.shape[0]):
        for y in range(0,output_img.shape[1]):
            output_img[x,y]=oneStep(new_img[x:x+f,y:y+f],filter1)
    return output_img

def averageFilter(size):
    filter1=np.ones((size,size),dtype=np.uint8)
    filter1=filter1/filter1.sum()
    return filter1

def gaussianFilter(size,sigma):
    m = size//2
    n = size//2
    gaussian_filter = np.zeros((size,size))
    for x in range(-m, m+1):
        for y in range(-n, n+1):
            x1 = 2*np.pi*(sigma**2)
            x2 = np.exp(-(x**2 + y**2)/(2* sigma**2))
            gaussian_filter[x+m, y+n] = (1/x1)*x2
    return gaussian_filter

def rotateFilter(filter1):
    return np.rot90(filter1,2);

def normalize(image):
    new_image=((image-np.min(image))*255)/(np.max(image)-np.min(image))
    new_image=new_image.astype(np.uint8)
    return new_image

filter1=np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
filter2=np.array([[1,1,1],[0,0,0],[-1,-1,-1]])



# image=cv.imread('canny_practice.png',0)
# vertical_edge=ApplyFilter(image, filter2)
# horizontal_edge=ApplyFilter(image, filter1)
# new_img=np.zeros(vertical_edge.shape)
# new_img=np.multiply(vertical_edge,vertical_edge)+np.multiply(horizontal_edge,horizontal_edge)
# new_img=new_img**(1/2)
# new_img=normalize(new_img)
# vertical_edge=normalize(vertical_edge)
# horizontal_edge=normalize(horizontal_edge)


# plt.subplot(141), plt.axis('off'), plt.imshow(image,cmap='gray'), plt.title('Original')
# plt.subplot(142), plt.axis('off'), plt.imshow(vertical_edge,cmap='gray'), plt.title('vertical')
# plt.subplot(143), plt.axis('off'), plt.imshow(horizontal_edge,cmap='gray'), plt.title('horizontal')
# plt.subplot(144), plt.axis('off'), plt.imshow(new_img,cmap='gray'), plt.title('Magnitude')
# plt.show()
# plt.close()


# cv.imshow("combined",new_img)

# cv.imshow('Horizontal_edges', vertical_edge)
# cv.imshow('vertical_edges', horizontal_edge)
# cv.waitKey(0)
# cv.destroyAllWindows()