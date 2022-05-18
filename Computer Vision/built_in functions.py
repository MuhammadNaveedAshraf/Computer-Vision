# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:49:23 2020

@author: emnas
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from skimage.util import random_noise
import random

img = cv.imread('xray.jpg',0)
gauss = random_noise(img, mode='gaussian')
salt_pepper = random_noise(img, mode='s&p')
poisson =random_noise(img,mode='poisson')
speckle=random_noise(img,mode='speckle')

def periodic(img,scale):
    noisy_img=np.zeros(img.shape)
    
    seq=0,1
    axis=random.choice(seq)
    for i in range(0,img.shape[axis]):
        random_no=random.random()
        if axis==0:
            noisy_img[i,:]=(noisy_img[i,:]+random_no)*scale
        else:
            noisy_img[:,i]=(noisy_img[:,i]+random_no)*scale
    noisy_img=noisy_img.astype(np.uint8)
    return noisy_img
def periodic2(img,minIntensity,maxIntensity,scale):
    noisy_img=np.zeros(img.shape)
    
    seq=0,1
    axis=random.choice(seq)
    random_no=random.randrange(minIntensity,maxIntensity,1)
    for x in range(0,img.shape[axis],scale+scale):
        for i in range(x,x+scale):
            if(x+scale<img.shape[axis]):            
                #print(random_no)
                if axis==0:
                    noisy_img[i,:]=(noisy_img[i,:]+random_no)
                else:
                    noisy_img[:,i]=(noisy_img[:,i]+random_no)
    noisy_img=noisy_img.astype(np.uint8)
    noisy_img=cv.add(noisy_img,img)
    return noisy_img
# noisy_img=periodic(img,50)
# image=cv.add(img,noisy_img)
# plt.imshow(image,cmap='gray')
# plt.show()
# plt.close()
image=periodic2(img,0,255,1)

plt.subplot(231), plt.axis('off'), plt.imshow(img,cmap='gray'), plt.title('Origin')
plt.subplot(232), plt.axis('off'), plt.imshow(gauss,cmap='gray'), plt.title('Gaussian')
plt.subplot(233), plt.axis('off'), plt.imshow(salt_pepper,cmap='gray'), plt.title('Salt & Pepper')
plt.subplot(234), plt.axis('off'), plt.imshow(poisson,cmap='gray'), plt.title('poisson')
plt.subplot(235), plt.axis('off'), plt.imshow(speckle,cmap='gray'), plt.title('speckle')
plt.subplot(236),plt.axis('off'),plt.imshow(image,cmap='gray'),plt.title('periodic')
plt.show()
plt.close()


  


  