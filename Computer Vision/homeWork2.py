# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import imageio as io
import numpy as np
import matplotlib.pyplot as plt


def colorToGray01(image):                                   # convert color image to grey scale using loop
    im=io.imread(image)
    im2=np.zeros((im.shape[0],im.shape[1]),dtype='int')
    for x in range(0,im.shape[0]):
        for y in range(0,im.shape[1]):
            im2[x,y]+=im[x,y,0]*0.299+im[x,y,1]*0.587+im[x,y,2]*0.114
    print(im2.shape)
    return im2



def appendImages(image1,image2):
    im = colorToGray01(image1)
    image =colorToGray01(image2)
    im2=np.append(np.append(im,np.dot(np.ones((im.shape[0],20),dtype='int'),255),axis=1),image,axis=1)   #concatenate two images
    return im2




def appendImages01(image1,image2):
    image01=io.imread(image1)#colorToGray01(image1)
    image02=io.imread(image2)#colorToGray01(image2)
    image03=np.zeros((image01.shape[0],image01.shape[1]+image02.shape[1]+20),dtype='int')
    for x in range (0,image01.shape[0]):
        for y in range (0,image01.shape[1]+20+image02.shape[1]):
            if (y>= image01.shape[1] and y<image01.shape[1]+20):    #for white line seperator
                image03[x][y]=255
            elif y<image01.shape[1]:                                #for first image 
                image03[x][y]= image01[x][y][0]
            elif y>=image01.shape[1]+20:                            #for second image
                image03[x][y]= image02[x][y-20-image01.shape[1]][0]
   
    return image03   


plt.imshow(appendImages01('01.jpg','02.jpg'), cmap="gray")
plt.show()


