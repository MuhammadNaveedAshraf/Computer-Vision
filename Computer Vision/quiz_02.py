# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:18:48 2020

@author: emnas
"""
import numpy as np
#import imageio as io
import matplotlib.pyplot as plt
import cv2 as cv
max_value=255
im=cv.imread('moon.jpeg',0)

#Remove text
for x in range(300,350):
    for y in range(0,1000):
        im[x,y]=0

for x in range(630,670):
    for y in range(0,1000):
        im[x,y]=0
for x in range(980,1050):
    for y in range(0,1000):
        im[x,y]=0
plt.imshow(im,cmap='gray')
plt.show()
plt.close()
        
for image in range(0,9):
    if image==0:
        im[:300,:400]=cv.adaptiveThreshold(im[:300,:400],max_value,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,131,-1)
    if image==1:
        im[:300,400:670]=cv.adaptiveThreshold(im[:300,400:670],max_value,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,131,-1)        
    if image==2:
        im[:300,670:1080]=cv.adaptiveThreshold(im[:300,670:1080],max_value,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,121,-1)
    if image==3:
        im[300:630,:400]=cv.adaptiveThreshold(im[300:630,:400],max_value,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,131,-1)
    if image==4:
        im[300:630,400:670]=cv.adaptiveThreshold(im[300:630,400:670],max_value,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,131,-1)        
    if image==5:
        im[300:630,670:1080]=cv.adaptiveThreshold(im[300:630,670:1080],max_value,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,131,-1)
    if image==6:
        im[630:1050,:400]=cv.adaptiveThreshold(im[630:1050,:400],max_value,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,131,-1)
    if image==7:
        im[630:1050,400:670]=cv.adaptiveThreshold(im[630:1050,400:670],max_value,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,131,-1)        
    if image==8:
        im[630:1050,670:1080]=cv.adaptiveThreshold(im[630:1050,670:1080],max_value,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,131,-1)        

# tresh=0;
# previous=0;
# firstTime=True
# counts,bins,patches=plt.hist(im.ravel(),bins=100)
# print
# for a in range(0,counts.size):
#     if firstTime:
#         tresh=a
#         previous=counts[a]
#         firstTime=False
#     elif counts[a]<=previous:
#         tresh=a
#         previous=counts[a]
#     else:
#         break
    

        
# plt.show()
# plt.close()
# thresh=60
# ret,des1=cv.threshold(im,thresh,max_value,cv.THRESH_BINARY)
# plt.imshow(des1,cmap="gray")
# plt.show()
# plt.close()
# print (tresh)
# image=np.zeros(im.shape,np.uint8)
# for i in range(0,im.shape[0]):
#     for j in range(0,im.shape[1]):
#         if(im[i,j]<tresh):
#             image[i,j]=0
#         else:
#             image[i,j]=255
# for x in range(0,1050):
#     for y in range(0,1050):
#         if(image[x,y]!= image[x+1,y]):
        

# plt.imshow(image,cmap='gray')
# plt.show()
# plt.close()
plt.imshow(im,cmap='gray')
plt.show()
plt.close()

