# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:00:57 2020

@author: emnas
"""
import matplotlib.pyplot as plt
import cv2 as cv
import imageio as io
import numpy as np
im= io.imread('original.png')
thresh=190
max_value=255
#ret,des=cv.threshold(im,thresh,max_value,cv.THRESH_BINARY_INV)

des=cv.adaptiveThreshold(im,max_value,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,601,-15)
plt.imshow(des,cmap="gray")
plt.show()
plt.close()
des1=cv.adaptiveThreshold(im,max_value,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,351,-17)   #perfectly matching
#des=cv.adaptiveThreshold(im,max_value,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,2) 
plt.imshow(des1,cmap="gray")
plt.show()
plt.close()
ret,des1=cv.threshold(im,thresh,max_value,cv.THRESH_BINARY_INV)
plt.imshow(des1,cmap="gray")
plt.show()
plt.close()

plt.imshow(im,cmap="gray")
plt.show()
plt.close()

eq_img=cv.equalizeHist(im)
cv.imshow('Equilized image',eq_img)
cv.waitKey(0)
cv.destroyAllWindows()