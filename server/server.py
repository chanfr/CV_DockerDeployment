#!flask/bin/python
import argparse
import logging

import cv2
from flask import Flask, jsonify
from flask import abort
from flask import request
from flask import send_file

from DockerDeployment.ImageRetriever import *

recogActive = False
recog = None
lenetActive = False
lenet = None
face_cascadeLoaded = False
face_cascade = None
eye_cascade = None

app = Flask(__name__)


@app.route('/')
def index():
    return "Server is running", 200


@app.route('/process', methods=['POST'])
def process_lenet():
    if lenetActive:
        try:
            global lenet
            if lenet == None:
                from DockerDeployment import Lenet
                weightsPath = "../DockerDeployment/weights/trained.hd5"
                lenet = Lenet.LeNet(weightsPath=weightsPath)
            imageKey = "media"
            data = {}
            if request.method == 'POST' and imageKey in request.files:
                image = ImageRetriever.getImage(request, imageKey)
                prediction = lenet.predict(image)
                data["prediction"] = int(prediction[0])
                return jsonify(data), 200
            else:
                abort(500)
        except Exception as e:
            error_msg = "Error at process_lenet: " + str(e)
            logging.error(error_msg)
            return error_msg, 404
    else:
        return "Lenet is not active on server", 500


@app.route('/get_size', methods=['POST'])
def getSize():
    imageKey = "media"
    if request.method == 'POST' and imageKey in request.files:
        image = ImageRetriever.getImage(request, imageKey)
        data = {}
        try:
            shape = image.shape
            h = shape[0]
            w = shape[1]
            if len(shape) == 3:
                c = shape[2]
            else:
                c = 1
        except Exception as e:
            logging.error("Error on get_size {}", e)
            abort(500)
        return jsonify(data), 200
    else:
        abort(500)


@app.route('/face_detection', methods=['POST'])
def laplacian():
    if not face_cascadeLoaded:
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    imageKey = "media"
    if request.method == 'POST' and imageKey in request.files:
        image = ImageRetriever.getImage(request, imageKey)
        if len(image.shape) > 2:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = image[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        pil_img = Image.fromarray(image.astype(np.uint8))
        img_io = BytesIO()
        pil_img.save(img_io, 'JPEG', quality=70)
        img_io.seek(0)
        return send_file(img_io, mimetype='image/jpeg')

    else:
        abort(500)


def parseArguments():
    parser = argparse.ArgumentParser(description='Lorem Ipsum')
    parser.add_argument('-l', '--lenet', type=bool, help='Lenet selected', required=False, default=False)
    parser.add_argument('-r', '--recog', type=bool, help='Recog selected', required=False, default=False)

    return parser.parse_args()


if __name__ == '__main__':
    opts = parseArguments()
    print(opts.lenet)
    print(opts.recog)

    if opts.lenet:
        lenetActive = True
    elif opts.recog:
        recogActive = True

    app.run(host="0.0.0.0", debug=True, threaded=True)
