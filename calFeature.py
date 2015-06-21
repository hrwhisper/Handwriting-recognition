# -*-coding:utf-8 -*-
'''
author:  hrwhipser
date   :  Jun 5, 2015
function : calculate feature and save in ./data/feature.txt ./data/tag.txt
'''
import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.filter import threshold_otsu
import skimage.io
from skimage import transform,measure
from sklearn import svm, metrics
from math import floor,ceil
from sklearn.externals import joblib

sameSize = 16


def readImage(fileName):
    image = skimage.io.imread(fileName, as_grey=True)
    threshold =  threshold_otsu(image)
    return image < threshold


def toTheSameSize(image):
    def findMinRange(image):
        up, down, left, right = image.shape[0], 0, image.shape[1], 0
        for i in xrange(image.shape[0]):
            for j in xrange(image.shape[1]):
                if image[i][j]:
                    up, down, left, right = min(up, i), max(down, i), min(left, j), max(right, j)
        return up, down, left, right
    up, down, left, right = findMinRange(image)
    image = image[up:down, left:right]
    image = transform.resize(image, (sameSize, sameSize))
    return image

def getTrainData(dataPath):
    files = os.walk(dataPath).next()[2]
    train_input , desired_output = [] , []
    for i , file in enumerate(files):
        outCharacter = file.split('_')[-2]
        if outCharacter.isdigit():continue
        testImg = toTheSameSize(readImage(dataPath+'\\'+file))
        train_input.append(testImg.ravel())
        desired_output.append(outCharacter)
        print i
        '''
        test = toTheSameSize(readImage(dataPath+'\\'+file))
        ax = plt.subplot(5,2,i+1)
        ax.set_axis_off() 
        ax.imshow(test)
        train_input.append(test)
        '''
    return train_input,desired_output



dataPath = r'F:\handwritingData7'

train_input,desired_output=getTrainData(dataPath)
print len(train_input)
with open('feature.txt','a+') as f:
    np.savetxt(f,train_input)
with open('tag.txt','a+') as f:
    f.write('\n'.join(desired_output))
    f.write('\n')
  
dataPath = r'F:\handwritingData0'

train_input,desired_output=getTrainData(dataPath)
print len(train_input)
with open('feature.txt','a+') as f:
    np.savetxt(f,train_input)
with open('tag.txt','a+') as f:
    f.write('\n'.join(desired_output))
    f.write('\n')
    
