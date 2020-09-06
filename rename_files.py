# rename files
import cv2 as cv
import matplotlib.pyplot as plt
from glob import glob
import os
import pickle
import numpy as np

clouds = {'altostratus':0, 'cumulus':1, 'cumulonimbus':2, 'altocumulus':3,
          'stratocumulus':4, 'cirrostratus':5, 'stratus':6, 'nimbostratus':7,
          'cirrus':8, 'cirrocumulus':9}
clouds_inv = {v: k for k, v in clouds.items()}

def splitfn(fn):
    path, fn = os.path.split(fn)
    name,ext = os.path.splitext(fn)
    return path, name, ext

for f in range(3,10):
    folder = clouds_inv[f] + '/'
    fnames = folder + "*-*.jpeg" # default
    paths = sorted(glob(fnames))
    indexed = sorted(glob(folder+"*us_????.jp*"))
    last = indexed[-1]
    fl,n,e = splitfn(last)
    lastindex = int(n[-4:])
    print(lastindex)
    for path in paths:
        folderr,name,ext = splitfn(path)
        img = cv.imread(path,1)
        lastindex += 1
        cv.imwrite(fl+'/'+clouds_inv[f]+'_%04d'%lastindex + '.jpg',img)
        os.remove(path)
