# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import imageio as io
import numpy as np
def colorToGrey01(image):
    im=io.imread(image)
    im2=np.zeros((im.shape[0],im.shape[1]),dtype='int')
    print(im.shape)
    print(im.shape[0],im.shape[1])
    for channel in range(0,2):
        for x in range(0,im.shape[0]):
            for y in range(0,im.shape[1]):
                if channel==0:
                    im2[x,y]+=im[x,y,channel]*0.29
                elif channel==1:
                    im2[x,y]+=im[x,y,channel]*0.58
                else:
                    im2[x,y]+=im[x,y,channel]*0.11
    return im2
            
#plt.imshow(colorToGrey01('01.jpg'),cmap='gray')
#plt.show()
def appendImages(image1,image2):
    image01=colorToGrey01(image1)
    image02=colorToGrey01(image2)
    image03=np.zeros((image01.shape[0],image01.shape[1]+image02.shape[1]+20),dtype='int')
    for x in range (0,image01.shape[0]):
        for y in range (0,image01.shape[1]):
            image03[x][y]= image01[x][y]
    for x in range (0,image01.shape[0]):
        for y in range (image01.shape[1],image01.shape[1]+20):
            image03[x][y]=255
    for x in range (0,image02.shape[0]):
        for y in range (0,image02.shape[1]):
            image03[x][y+20+image01.shape[1]]= image02[x][y]
    return image03   
        
plt.imshow(appendImages('01.jpg','02.jpg'),cmap='gray')
plt.show()



def colorToGrey00(image):                                  # convert color image to grey scale using advanced processing
    im = io.imread(image)
    print("image shape before"+str(im.shape))
    print("No of channels in the image are "+str(im.shape[2]))
    im1=np.zeros((im.shape[0],im.shape[1]))
    im1=(im[:,:,0]*0.299+im[:,:,1]*0.587+im[:,:,2]*0.114)
    print("image shape after"+str(im1.shape))
    plt.imshow(im1)
    return im1
#plt.imshow(colorToGrey01("Wall.jpg"))