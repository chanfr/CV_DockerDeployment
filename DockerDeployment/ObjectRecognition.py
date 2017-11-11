
from keras.applications.mobilenet import MobileNet
from keras.preprocessing import image as image_utils
import numpy as np
from keras.applications.mobilenet import *
import cv2




class ObjectRecognition:
    def __init__(self):
        self.model = MobileNet(weights="imagenet")
        self.inputImageSize=(244,244)


    def processImage(self,image_in):
        image=cv2.resize(image_in,self.inputImageSize)
        image = image.transpose((2, 0, 1))
        image = preprocess_input(image.astype(float))
        image = np.expand_dims(image, axis=0)

        preds = self.model.predict(image)
        for pred in preds:
            print pred
        (inID, label) = decode_predictions(preds)[0]
        # origin = cv2.imread(file)
        # cv2.putText(origin, "Predict: {}".format(label), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        # cv2.imshow("Result", origin)
