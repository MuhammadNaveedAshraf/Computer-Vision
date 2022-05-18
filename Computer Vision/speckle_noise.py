# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:52:43 2020

@author: emnas
"""
import numpy as np
import random
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('original.png',0)
r,c = img.shape
speckle_noise = np.random.normal(0,1,img.shape)
speckle_noise= speckle_noise.astype(np.uint8)
noisy_img =  img + img * speckle_noise
noisy_img = noisy_img.astype(np.uint8)      
cv.imshow('Speckle',noisy_img)
cv.waitKey(0)
cv.destroyAllWindows()
