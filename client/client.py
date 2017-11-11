import requests
import json
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
import cv2
import StringIO
from PIL import Image


def getMNISImage():
    dataset = datasets.fetch_mldata("MNIST Original")
    data = dataset.data.reshape((dataset.data.shape[0], 28, 28))
    data = data[:, np.newaxis, :, :]
    (trainData, testData, trainLabels, testLabels) = train_test_split(
        data / 255.0, dataset.target.astype("int"), test_size=0.33)

    idx=np.random.choice(np.arange(0, len(testLabels)))
    image=testData[np.newaxis, idx][0][0]
    image = (image * 255).astype("uint8")
    return image


def process_lenet(host,port):
    url="{}:{}/process".format(host,port)
    image=getMNISImage()
    imagePath="test_image.png"
    cv2.imwrite(imagePath,image)
    files = {'media': open(imagePath, 'rb')}
    data=requests.post(url, files=files)


    responseData=json.loads(data.content)
    image = cv2.resize(image, (96, 96), interpolation=cv2.INTER_LINEAR)
    image =cv2.cvtColor(image,cv2.COLOR_GRAY2BGR )
    cv2.putText(image, str(responseData["prediction"]), (5, 20),
    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    cv2.imshow("Result",image)
    cv2.waitKey(0)



def test():
    image=getMNISImage()
    cv2.imshow("testInput")
    imagePath='/mnt/large/pentalo/deep/datasets/voc/original_format/VOCdevkit/VOC2007/JPEGImages/000001.jpg'


    files = {'media': open(imagePath, 'rb')}
    data=requests.post(url, files=files)

    responseData=json.loads(data.content)
    print responseData


def main():
    host="http://localhost"
    port="5000"
    process_lenet(host,port)


if __name__ == "__main__":
    main()