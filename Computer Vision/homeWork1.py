# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:45:16 2020

@author: emnas
"""
import numpy as np
import imageio as io
import matplotlib.pyplot as plt


def colorToGrey(image):
    im = io.imread(image)
    print("No of channels in the image are "+str(im.shape[2]))
    #im1=np.zeros((im.shape[0],im.shape[1]))
    im1=(im[:,:,0]*0.299+im[:,:,1]*0.587+im[:,:,2]*0.114)
    return im1



def colorToGrey01(image):                                  # convert color image to grey scale using loop
    im=io.imread(image)
    im2=np.zeros((im.shape[0],im.shape[1]),dtype='int')
    print("No of channels in the image are "+str(im.shape[2]))
    for x in range(0,im.shape[0]):
        for y in range(0,im.shape[1]):
                    im2[x,y]+=im[x,y,0]*0.299+im[x,y,1]*0.587+im[x,y,2]*0.114
    print(im2.shape)
    return im2



im = colorToGrey('Picture1.jpg')
plt.imshow(im, cmap="gray")
plt.show()
#image =colorToGrey01(Image.open("IMG_0184.jpg"))