# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:45:23 2020

@author: emnas
"""
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
im1=cv.imread('xray.png',0)
q=8;
l=cv.imread('xray.png',0)
mp=(2**q)-1
a= l.min()
b=l.max()
R=b-a
print(l.min(),l.max())
plt.hist(l,bins=100)
plt.show()
plt.close()
for x in range(0,l.shape[0]):
    for y in range(0,l.shape[1]):
        l[x,y]=((l[x,y]-a)/R)*mp
        l[x,y]=np.round(l[x,y])

plt.hist(l,bins=100)
plt.show()
plt.close()
print(l.min(),l.max())
# plt.imshow(l,cmap="gray")
# plt.show()
# plt.close()
equ_img= cv.equalizeHist(im1)
ret,bin_l=cv.threshold(l,170,255,cv.THRESH_BINARY_INV)
ret1,bin_equ=cv.threshold(equ_img,170,255,cv.THRESH_BINARY_INV)
plt.subplot(231), plt.axis('off'), plt.imshow(im1,cmap='gray'), plt.title('Original')
plt.subplot(232), plt.axis('off'), plt.imshow(l,cmap='gray'), plt.title('preprocessed')    
plt.subplot(233), plt.axis('off'), plt.imshow(bin_l,cmap='gray'), plt.title('Binary')
plt.subplot(234), plt.axis('off'), plt.imshow(im1,cmap='gray'), plt.title('Original')
plt.subplot(235), plt.axis('off'), plt.imshow(equ_img,cmap='gray'), plt.title('preprocessed')
plt.subplot(236), plt.axis('off'), plt.imshow(bin_equ,cmap='gray'), plt.title('Binary')
# cv.imshow('Binary Image', equ_img)
# cv.waitKey(0)
# cv.destroyAllWindows()
