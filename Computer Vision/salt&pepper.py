# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:22:32 2020

@author: emnas
"""
import numpy as np
import random
import cv2
img = cv2.imread('original.png',0)

def salt_pepper(img):
    noisy_img = np.zeros(img.shape,np.uint8)
    prob_of_noise=0.08
    thres = 1 - prob_of_noise
    r,c = img.shape 
    for i in range(r):
        for j in range(c):
            random_no = random.random()
            if random_no < prob_of_noise:
                noisy_img[i][j] = 0
            elif random_no > thres:
                noisy_img[i][j] = 255
            else:
                noisy_img[i][j] = img[i][j]
    return noisy_img
noisy_img=salt_pepper(img);
cv2.imshow('salt_pepper_noise',noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

