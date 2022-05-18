# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 15:11:18 2021

@author: emnas
"""
import numpy as np
def pad(filterSize):
    p=(filterSize-1)/2
    return int(p)

def applyPad0(pad,image):
    x,y=image.shape
    x=int(x+(2*pad))
    y=int(y+(2*pad))
    img=np.zeros((x,y))
    img[pad:x-pad,pad:y-pad]=image
    return img
def mean(patch):
    return np.mean(patch)
def median(patch):
    return np.median(patch);
def variance(patch):
    return np.var(patch)
def standardDeviation(patch):
    return np.std(patch);
def skewness(patch,mean,std):
    N=patch.shape[0]*patch.shape[1]
    skew=0
    for x in range(0,patch.shape[0]):
        for y in range(0,patch.shape[1]):
            skew+=((patch[x,y]-mean)/std,3)
    if(std != 0):
        skew=skew/N
    return skew
def kurtosis(patch,mean,std):
    N=patch.shape[0]*patch.shape[1]
    kurt=0
    for x in range(0,patch.shape[0]):
        for y in range(0,patch.shape[1]):
            kurt+=pow((patch[x,y]-mean)/std,4)
    if(std != 0):
        kurt=kurt/N
    return kurt
def mad(patch,mean):
    return np.mean(patch-mean)
def mead(patch,mad):
    return np.median(patch-mad)
def localContrast(patch):
    return np.max(patch) - np.min(patch)
def localProb(patch):
    x,y=patch.shape
    k=patch[int((x+1)/2),int((y+1)/2)]
    kthCount=0
    for row in patch:
        for index in row:
            if(index==k):
                kthCount+=1
    return kthCount/(x*y) 
def percentile(patch):
    N=patch.shape[0]*patch.shape[1]
    sortedPatch=np.sort(patch.flatten())
    return sortedPatch[int(np.round(N*0.25))]
def percentile1(patch):
    N=patch.shape[0]*patch.shape[1]
    sortedPatch=np.sort(patch.flatten())
    return sortedPatch[int(np.round(N*0.75))]
output=percentile(np.array([[1,2,3],[2,5,4],[5,0,0]]))