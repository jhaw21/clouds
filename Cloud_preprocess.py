# Cloud preprocessor
import cv2 as cv
import matplotlib.pyplot as plt
from glob import glob
import os
import pickle
import numpy as np

folder = "*s/"
##
##folders = glob(folder)
###for f in folders:
###    os.mkdir(f+"112x112")
##
prefix = "*s_????"
fnames = folder + prefix + ".jp*" # default
paths = sorted(glob(fnames))

def splitfn(fn):
    path, fn = os.path.split(fn)
    name,ext = os.path.splitext(fn)
    return path, name, ext

shapes = []
for path in paths:
   img = cv.imread(path,1)
   h,w,c = img.shape

   s = min(h,w)
   square = img[0:s,0:s,:]
   new = cv.resize(square,(112,112))

   fldr, name, ext = splitfn(path)
   cv.imwrite(fldr+"/112x112/"+name+'.png',new)

##os.mkdir("test")
##os.mkdir("train")

clouds = {'altostratus':0, 'cumulus':1, 'cumulonimbus':2, 'altocumulus':3,
          'stratocumulus':4, 'cirrostratus':5, 'stratus':6, 'nimbostratus':7,
          'cirrus':8, 'cirrocumulus':9}

paths = sorted(glob("*s/112x112/*.png"))
trainLabels = []
testLabels = []
testc = 0
trainc = 0
test_images = []
train_images = []

for i in range(0,len(paths)):
    path = paths[i]
    img = cv.imread(path,1)
    fldr, name, ext = splitfn(path)

    cloudType = name.split('_')[0]
    if i%5==0:
        one_hot = np.zeros(10)
        one_hot[clouds[cloudType]] = 1
        testLabels.append(one_hot)
        cv.imwrite("test/cloud_%04d"%testc+'.png',img)
        test_images.append(img)
        testc+=1
    else:
        one_hot = np.zeros(10)
        one_hot[clouds[cloudType]] = 1
        trainLabels.append(one_hot)
        cv.imwrite("train/cloud_%04d"%trainc+'.png',img)
        train_images.append(img)
        trainc+=1

fout = open("trainLabels.pickle", "wb")
pickle.dump(trainLabels, fout)
fout.close()

fout = open("testLabels.pickle", "wb")
pickle.dump(testLabels, fout)
fout.close()

fout = open("test_images.pickle", "wb")
pickle.dump(test_images, fout)
fout.close()

fout = open("train_images.pickle", "wb")
pickle.dump(train_images, fout)
fout.close()


