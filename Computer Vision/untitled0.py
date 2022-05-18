# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 20:39:33 2021

@author: emnas
"""
import numpy as np

def substring2(string):
    if(len(string)%2 is 0):
        subStr1=string[:int(len(string)/2)]
        subStr2=string[int(len(string)/2):]
        if(subStr1==subStr2):
            return subStr1
        elif(subStr1!=subStr2):
            for x in range(2,len(subStr1)):
                subStr2=subStr1[-1]+subStr2[:-2]
                subStr1=subStr1[:-1]
                if(subStr1==subStr2 and len(string)%len(subStr1)==0):
                    return subStr1
            return -1
                #x=x+1

    else:
        subStr1=string[:int(len(string)/3)]
        subStr2=string[int(len(string)/3):int(len(string)*(2/3))]
        if(subStr1==subStr2 and len(string)%len(subStr1)==0):
            return subStr1
        elif(subStr1!=subStr2):
            for x in range(2,len(subStr1)):
                subStr2=subStr1[-1]+subStr2[:-2]
                subStr1=subStr1[:-1]
                if(subStr1==subStr2 and len(string)%len(subStr1)==0):
                    return subStr1
                #x=x+1
            return -1
           
def substring(string):
    if(len(string)%2 is 0):
        subStr1=string[:int(len(string)/2)]
        subStr2=string[int(len(string)/2):]

    else:
        subStr1=string[:int(len(string)/3)]
        subStr2=string[int(len(string)/3):int(len(string)*(2/3))]
    if(subStr1==subStr2 and len(string)%len(subStr1)==0):
        return subStr1
    elif(subStr1!=subStr2):
        for x in range(2,len(subStr1)):
            subStr2=subStr1[-1]+subStr2[:-2]
            subStr1=subStr1[:-1]
            if(subStr1==subStr2 and len(string)%len(subStr1)==0):
                return subStr1
            #x=x+1
        return -1
            
#    print(subStr1,subStr2)
 
def maxSum(array):
    output= sum(array)
    for x in range(0,len(array)):
        if(array[0]>array[-1]):
            array=array[:-1]
        else:
            array=array[1:]
        if(sum(array)>output):
            output=sum(array)
    return output
   
#output=substring('abababab')
#print(output)
print(maxSum([3,-1,-1,4,3,-1]))