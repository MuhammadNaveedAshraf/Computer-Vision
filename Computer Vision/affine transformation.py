# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 19:14:52 2020

@author: emnas
"""
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from Bilinear_Interpolation import Bilinear_Interpolation
# x1,y1=0,30
# x2,y2=0,2369
# x3,y3=2399,2369
# x1_,y1_=30,2399
# x2_,y2_=2369,2399
# x3_,y3_=2369,0
image=cv.imread('image 1.jpg',0)
x,y=image.shape
x1,y1=0,0
x2,y2=0,1
x3,y3=1,1
x1_,y1_=0,1
x2_,y2_=1,1
x3_,y3_=1,0

A=np.array([[x1,y1,1,0,0,0],[0,0,0,x1,y1,1],[x2,y2,1,0,0,0],[0,0,0,x2,y2,1],[x3,y3,1,0,0,0],[0,0,0,x3,y3,1]])
b=np.array([[x1_],[y1_],[x2_],[y2_],[x3_],[y3_]])
if(A.shape[0]==A.shape[1]):
    X=np.dot(np.linalg.inv(A),b)
else:
    X=np.dot(np.dot(np.linalg.inv(np.dot(A.transpose(),A)),A.transpose()),b)
#generating affine matrix from 
affine_matrix=np.array([[X[0][0],X[1][0],X[2][0]],[X[3][0],X[4][0],X[5][0]],[0,0,1]])

#get size for transformed image  using X'=AX where using X as image dimension
l,m,n=abs(np.dot(affine_matrix,np.array([[image.shape[0]],[image.shape[1]],[1]]))).astype(np.int32)
transformed_image=np.zeros((l[0],m[0]),dtype=np.int32)

for i in range(0,x):
    for j in range(0,y):
        l,m,n=np.dot(affine_matrix,np.array([[i],[j],[1]]))
        l=(l.astype('int32'))
        m=(m.astype('int32'))
        transformed_image[l,m]=image[i,j]

transformed_image=Bilinear_Interpolation(transformed_image,450,450)        
plt.imshow(image, cmap='gray')
plt.show()
plt.close()
plt.imshow(transformed_image, cmap='gray')
plt.show()
plt.close()
