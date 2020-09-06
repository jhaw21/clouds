from keras.models import load_model
import numpy as np
import cv2 as cv

def predict(img):
    model1 = load_model("cnn.h5")
    img = np.reshape(img,[1,256,256,3])

    clouds = {'altostratus':0, 'cumulus':1, 'cumulonimbus':2, 'altocumulus':3,
            'stratocumulus':4, 'cirrostratus':5, 'stratus':6, 'nimbostratus':7,
            'cirrus':8, 'cirrocumulus':9}
    iCloud = {value: key for key, value in clouds.items()}

    hola = model1.predict_classes(img)[0]
    ciao = iCloud[hola]
    return ciao

def predict_many(img_array):
    return_array = []
    model1 = load_model("cnn.h5")
    clouds = {'altostratus':0, 'cumulus':1, 'cumulonimbus':2, 'altocumulus':3,
                'stratocumulus':4, 'cirrostratus':5, 'stratus':6, 'nimbostratus':7,
                'cirrus':8, 'cirrocumulus':9}
    iCloud = {value: key for key, value in clouds.items()}
    for index in range(0,len(img_array)):
        img = img_array[index]
        img = np.reshape(img,[1,256,256,3])

        hola = model1.predict_classes(img)[0]
        ciao = iCloud[hola]
        return_array.append(ciao)
    return return_array

index = 57
img = cv.imread("train/cloud_%04d.png"%index)

print(predict(img))