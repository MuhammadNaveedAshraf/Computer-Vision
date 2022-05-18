# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:42:41 2020

@author: emnas
"""

import numpy as np
import random
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('original.png',0)

noisy_img = np.zeros(img.shape,np.uint8)
poisson_noise=np.random.poisson(20,img.shape)

poisson_noise=poisson_noise.astype(np.uint8)
noisy_img = img + poisson_noise
cv2.imshow('poission',noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
