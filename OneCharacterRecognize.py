# -*-coding:utf-8 -*-
'''
author:  hrwhipser
date   :  May 13, 2015
'''

import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.filter import threshold_otsu
import skimage.io
from skimage import transform
from sklearn import svm, metrics
from sklearn.externals import joblib
from sklearn.neighbors import KNeighborsClassifier

sameSize = 16

class OneCharacterRecognize:
    def __init__(self, trainNum=70000, test_num=None , debug=False ,svm=True):
        self.dataPath = r'F:\handwritingData0'
        self.savePath = './data/handwritingData0.pkl'
        self.debug = debug
        self.svm = svm
        self.train_num = trainNum
        if debug:
            self.train_input = np.loadtxt("feature.txt")
            self.totNum = len(self.train_input)
            if test_num:self.test_num = test_num
            else: self.test_num = self.totNum - self.train_num
            self.desired_output = []
            with open('tag.txt', 'r') as f:
                for line in f:  self.desired_output.append(line.strip('\n'))
        
    def getTrainData(self, start, end):
        return self.train_input[start:end], self.desired_output[start:end]

    def getClassifier(self):
        if self.svm and not self.debug: return joblib.load(self.savePath) 
        train_input, train_output = self.getTrainData(0, self.train_num)
        if self.svm:  
            clf = svm.SVC(gamma=0.01)
            clf.fit(train_input,train_output)
            joblib.dump(clf, self.savePath)
            return clf
        else:  
            clf = KNeighborsClassifier(n_neighbors=3)
            clf.fit(train_input,train_output)
            return clf
    
    def predict(self,feature):
        clf = self.getClassifier()
        return clf.predict(feature)
