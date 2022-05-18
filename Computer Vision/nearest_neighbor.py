# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 23:11:19 2020

@author: emnas
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def implement(image,resizeRatio):
    x,y=image.shape
    new_x,new_y=int(round(resizeRatio*x)),int(round(resizeRatio*y))
    new_img=np.zeros((new_x,new_y))
    if(x < new_x):
        Sr=x/new_x
    elif(x>new_x):
        Sr=(x-1)/new_x
    if(y < new_y):
        Sc=x/new_x
    elif(y>new_y):
        Sc=(x-1)/new_x

    for i in range(0,new_x):
        for j in range(0,new_y):
            #print(x_img[i,j],y_img[i,j])
            if(round(i*(x/new_x))<x and round(j*(y/new_y))<y ):
                new_img[i,j]=image[round(i*Sr),round(j*Sc)]
    return  new_img
     
image=cv.imread('cube1.jpg',0)
new_img=implement(image,resizeRatio=2)
plt.imshow(image,cmap='gray')
plt.show()
plt.close()   
plt.imshow(new_img,cmap='gray')
plt.show()
plt.close()    