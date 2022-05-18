# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 22:51:05 2020

@author: emnas
"""
import imageio as io
import numpy as np
import matplotlib.pyplot as plt
#import cv2 as cv
#image=io.imread("navid.jpg")
def colorToGrey00(image):                                  # convert color image to grey scale using advanced processing
    im = io.imread(image)
    print("image shape before"+str(im.shape))
    print("No of channels in the image are "+str(im.shape[2]))
    im1=np.zeros((im.shape[0],im.shape[1]))
    im1=(im[:,:,0]*0.299+im[:,:,1]*0.587+im[:,:,2]*0.114)
    print("image shape after"+str(im1.shape))
    #plt.imshow(im1)
    return im1
image=colorToGrey00('flower.jpg')
#plt.close()
plt.hist(image.ravel(),bins=100)
plt.show()
plt.close()
image00=np.zeros((image.shape[0],image.shape[1]),dtype=np.uint8)

for i in range(0,image.shape[0]):
    for j in range(0,image.shape[1]):
        if(image[i,j]>=40):
            image00[i,j]=255
        else:
            image00[i,j]=0

plt.imshow(image00,cmap="gray")
plt.show()
plt.close()

image=colorToGrey00('flower1.jpg')
plt.hist(image.ravel(),bins=100)
plt.show()
plt.close()
image00=np.zeros((image.shape[0],image.shape[1]),dtype=np.uint8)

for i in range(0,image.shape[0]):
    for j in range(0,image.shape[1]):
        if(image[i,j]>=180):
            image00[i,j]=255
        else:
            image00[i,j]=0

plt.imshow(image00,cmap="gray")
plt.show()
plt.close()
print(image.shape)

image=io.imread('original.png')
plt.hist(image.ravel(),bins=100)
plt.show()
plt.close()
image00=np.zeros((image.shape[0],image.shape[1]),dtype=np.uint8)

for i in range(0,image.shape[0]):
    for j in range(0,image.shape[1]):
        if(image[i,j]>=190):
            image00[i,j]=255
        else:
            image00[i,j]=0

plt.imshow(image00,cmap="gray")
plt.show()
plt.close()
print(image.shape)





