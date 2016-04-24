# -*-coding:utf-8 -*-
'''
author:  hrwhipser
date   :  Jun 5, 2015
function : calculate feature and save in ./data/feature.txt ./data/tag.txt
'''
import os
import numpy as np
from handwriting_tools import read_image, to_the_same_size

sameSize = 16


def get_train_data(dataPath):
    files = os.walk(dataPath).next()[2]
    train_input, desired_output = [], []
    for i, file in enumerate(files):
        outCharacter = file.split('_')[-2]
        suffix = file.split('.')[-1]
        if outCharacter.isdigit() or suffix != 'bmp': continue
        testImg = to_the_same_size(read_image(dataPath + '\\' + file))
        train_input.append(testImg.ravel())
        desired_output.append(outCharacter)
        print i, file
        '''
        test = to_the_same_size(read_image(dataPath+'\\'+file))
        ax = plt.subplot(5,2,i+1)
        ax.set_axis_off() 
        ax.imshow(test)
        train_input.append(test)
        '''
    return train_input, desired_output


if __name__ == '__main__':
    # dataPath = r'F:\handwritingData7'
    dataPath = r'E:\sd_nineteen\HSF_7'

    train_input, desired_output = get_train_data(dataPath)
    print len(train_input)
    with open('feature.txt', 'a+') as f:
        np.savetxt(f, train_input)
    with open('tag.txt', 'a+') as f:
        f.write('\n'.join(desired_output))
        f.write('\n')

    # dataPath = r'F:\handwritingData0'
    dataPath = r'E:\sd_nineteen\HSF_0'

    train_input, desired_output = get_train_data(dataPath)
    print len(train_input)
    with open('feature.txt', 'a+') as f:
        np.savetxt(f, train_input)
    with open('tag.txt', 'a+') as f:
        f.write('\n'.join(desired_output))
        f.write('\n')
