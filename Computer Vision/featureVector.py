# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 21:28:45 2021

@author: emnas
"""
from FOSF import pad
from FOSF import applyPad0
from FOSF import mean
from FOSF import median
from FOSF import variance
from FOSF import mad
from FOSF import mead
from FOSF import localContrast
from FOSF import localProb
from FOSF import percentile
from FOSF import percentile1
from FOSF import standardDeviation
from FOSF import kurtosis
from FOSF import skewness
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def getFeatures(patch):
    _mean=mean(patch)
    _median=median(patch)
    _variance=variance(patch)
    std=standardDeviation(patch)
    _skewness= skewness(patch, _mean, std)
    _kurtosis= kurtosis(patch, _mean,std)
    localC=localContrast(patch)
    _localProb=localProb(patch)
    per=percentile(patch)
    per1=percentile1(patch)
    _mad=mad(patch,_mean)
    _mead=mead(patch, _mad)
    return np.array([_mean,_median,_variance,std,_skewness,_kurtosis,_mad,_mead,localC,_localProb,per,per1])

image=cv.imread("xray.jpg",0)
x=image.shape[0]
y=image.shape[1]
# patch is 3*3
patchsize=3
padSize=pad(patchsize)
newImage=applyPad0(padSize,image)
#patch size==3
x=x+2*padSize-patchsize+1
y=y+2*padSize-patchsize+1
featureVectors=np.zeros((x,y,12));
for x in range(0,featureVectors.shape[0]):
        for y in range(0,featureVectors.shape[1]):
            featureVectors[x,y,:]=getFeatures(newImage[x:x+patchsize,y:y+patchsize])
for z in range(0,10):
    cv.imshow("image",featureVectors[:,:,z])
    cv.waitKey(0)
#     return output_img
