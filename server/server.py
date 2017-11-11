#!flask/bin/python
from flask import Flask
from flask import request
from flask import abort
from flask import Flask, jsonify
from PIL import Image
import StringIO
import cv2
import numpy as np
from DockerDeployment.ImageRetriever import *
import logging
import argparse


recogActive=False
recog=None
lenetActive=False
lenet=None


app = Flask(__name__)

@app.route('/')
def index():
    return "Server is running",200



@app.route('/process', methods=['POST'])
def process_lenet():
    if lenetActive:
        try:
            global lenet
            if lenet == None:
                from DockerDeployment import Lenet
                weightsPath = "../DockerDeployment/weights/trained.hd5"
                lenet = Lenet.LeNet(width=28, height=28, depth=1, classes=10, weightsPath=weightsPath)
            imageKey = "media"
            data = {}
            if request.method == 'POST' and imageKey in request.files:
                image = ImageRetriever.getImage(request, imageKey)
                prediction = lenet.predict(image)
                data["prediction"]=prediction[0]
                return jsonify(data),200
            else:
                abort(500)
        except Exception as e:
            error_msg="Error at process_lenet: " + str(e)
            logging.error(error_msg)
            return error_msg,404
    else:
        return "Lenet is not active on server", 500



@app.route('/get_size', methods=['POST'])
def getSize():
    imageKey = "media"
    if request.method == 'POST' and imageKey in request.files:
        image = ImageRetriever.getImage(request, imageKey)
        data={}
        try:
            if len(image.shape)==3:
                h,w,c=image.shape
                data["width"]=w
                data["height"]=h
                data["channels"]=c
            else:
                h,w=image.shape
                data["width"]=w
                data["height"]=h
                data["channels"]=1
        except Exception, e:
            s = str(e)
            logging.error("Error on get_size" + s)
            abort(500)
        return jsonify(data),200
    else:
        abort(500)


@app.route('/get_objects', methods=['POST'])
def get_objects():
    if recog != None:
        imageKey = "media"
        if request.method == 'POST' and imageKey in request.files:
            image = ImageRetriever.getImage(request, imageKey)
            recog.processImage(image)


    else:
        return "Recog is not active on server", 500



def parseArguments():
    parser = argparse.ArgumentParser(description='Lorem Ipsum')
    parser.add_argument('-l', '--lenet', type=bool, help='Lenet selected', required=False, default=False)
    parser.add_argument('-r', '--recog', type=bool, help='Recog selected', required=False, default=False)

    return parser.parse_args()



if __name__ == '__main__':
    opts=parseArguments()
    print opts.lenet
    print opts.recog

    if opts.lenet:
        lenetActive=True
    elif opts.recog:
        recogActive=True

    app.run(host="0.0.0.0",debug=True)