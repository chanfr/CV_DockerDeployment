import json
from random import randint

import cv2
import mnist
import requests

from DockerDeployment.ImageSender import ImageSender


def getMNISImage():
    test_images = mnist.test_images()
    value = randint(0, test_images.shape[0])
    random_image = test_images[value]
    return random_image


def process_lenet(host, port, auto_mode, number_of_requests):
    for i in range(0, number_of_requests):
        url = "{}:{}/process".format(host, port)
        image = getMNISImage()
        ret = ImageSender.prepare_to_send(image)
        files = {'media': ("temp.png", ret)}
        data = requests.post(url, files=files)

        try:
            responseData = json.loads(data.content)
            image = cv2.resize(image, (96, 96), interpolation=cv2.INTER_LINEAR)
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
            cv2.putText(image, str(responseData["prediction"]), (5, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

            image2show = cv2.resize(image, (500, 500), interpolation=cv2.INTER_LINEAR)
            cv2.imshow("Result", image2show)
            if auto_mode:
                cv2.waitKey(50)
            else:
                cv2.waitKey(0)
        except:
            print("Error: {}".format(data.text))


def main():
    #host = "http://ec2co-ecsel-vgimzl5m1dpz-314581070.eu-west-3.elb.amazonaws.com"
    host = "http://localhost"
    port = "5000"
    auto_mode = True
    number_of_requests = 10000
    process_lenet(host, port, auto_mode, number_of_requests)


if __name__ == "__main__":
    main()
