# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 12:33:32 2020

@author: emnas
"""
import imageio as io
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# im=cv.imread('original.png',0)
# def findIndex(number,bins,bits):
#     value=np.floor(number*(bins/(2**bits)))
#     return np.uint8(value)

# def histogram(bins,bits,image):
#     im=cv.imread(image,0);
#     array=np.zeros((255),dtype=np.uint8)
#     binSize=(2**bits)/bins
# #    print(im.shape)
  
#     for x in range(0,im.shape[0]):
#         for y in range(0,im.shape[1]):
#             value=findIndex(im[x,y],bins,bits)
#             #value=np.uint8(np.floor(im[x,y]/(binSize)))
#             array[value]=array[value]+1
#     return array

# array=histogram(128,8,'original.png')
# plt.hist(array.ravel())
# print(findIndex(im[0][0],256,8))
# plt.show()
# plt.close()

# plt.hist(im.ravel())
# print(findIndex(im[0][0],256,8))
# plt.show()
# plt.close()

img=cv.imread('original.png',0)
gauss_noise=np.random.normal(0,1,img.shape)
gauss_noise= gauss_noise.astype(np.uint8)
#img= img.astype(np.float64) 
noisy_img=cv.add(img,gauss_noise)
plt.imshow(img,cmap="gray")
plt.show()
plt.close
plt.imshow(noisy_img,cmap="gray")
plt.show()
plt.close  