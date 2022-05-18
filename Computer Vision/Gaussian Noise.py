# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 09:31:07 2020

@author: emnas
"""
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('original.png',0)
gauss_noise=np.random.normal(0,1,img.shape)
gauss_noise=gauss_noise.astype(np.uint8)


noisy_img= cv.add(gauss_noise,img)
noisy_img=noisy_img.astype(np.uint8)
plt.imshow(gauss_noise,cmap='gray')
plt.show()
plt.close()
plt.imshow(noisy_img,cmap='gray')
plt.show()
plt.close()