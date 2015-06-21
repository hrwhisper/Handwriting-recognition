# -*-coding:utf-8 -*-
'''
author:  hrwhipser
date   :  May 22, 2015
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
from OneCharacterRecognize import OneCharacterRecognize 
from correctWord import CorrectWord
sameSize  = 16
wordSpace = 7

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

def getImageWords(image):
    #删除包含的区域，返回正确的区域
    def removeRange(cells):
        # b in a
        def rangeInclude(a,b):
            return b.up >= a.up and b.down <= a.down and b.left>=a.left and b.right<=a.right
        
        def rangeCmp(rangeDataA,rangeDataB):
            return -1 if rangeDataA.down - rangeDataA.up < rangeDataB.down - rangeDataB.up else 1
               
        cells.sort(rangeCmp)
        n = len(cells)
        ok = [True] * n
        for i in xrange(1,n):
            for j in xrange(i):
                if ok[j] and rangeInclude(cells[i],cells[j]):
                    ok[j] = False
        newCells = [cells[i] for i in xrange(n) if ok[i]]
        return newCells  
          
    #单词排序
    def mycmp(rangeDataA,rangeDataB):
        return -1 if rangeDataA.left < rangeDataB.left else 1
    
    contours = measure.find_contours(image, 0.8)
    cells = []
    for contour in contours:
        up,down,left,right = min(contour[:, 0]),max(contour[:, 0]),min(contour[:, 1]),max(contour[:, 1])
        if down - up >= wordSpace or right - left >= wordSpace:
            cells.append(rangeData(up,down,left,right))
    
    cells = removeRange(cells)
    cells.sort(mycmp)
    return cells

class rangeData:
    def __init__(self,up,down,left,right):
        self.up    =  floor(up)
        self.down  =  ceil(down)
        self.left  =  floor(left)
        self.right =  ceil(right)
    
    def __str__(self):
        return ' '.join(str(i) for i in [self.left])
    
    __repr__ = __str__
    
    def getInfo(self):
        return self.up,self.down,self.left,self.right


plt.gray()
clf = OneCharacterRecognize()
print 'read test file'
image = readImage('./data/test3.png')
word = getImageWords(image)
print len(word)
ans = []
for i , c in enumerate(word):
    nw,sw,ne,se = c.getInfo()
    cur = toTheSameSize(image[nw:sw,ne:se])
    ax  = plt.subplot(len(word),1,i+1)
    ax.imshow(cur)
    ax.set_axis_off()
    ans.append( clf.predict(cur.ravel())[0])
ans =''.join(ans)
print ans
cw = CorrectWord()
print cw.correct(ans.lower())
plt.show()