import os
import cv2
import numpy as np



def process(imagePath):
    image=cv2.imread(imagePath)
    shape=image.shape
    if len(shape)==2:
        image=cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



    corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
    corners = np.int0(corners)

    for i in corners:
        x, y = i.ravel()
        cv2.circle(image, (x, y), 3, (255,255,0), -1)


    filename, file_extension = os.path.splitext(imagePath)
    outImagePath=filename + "_processed"+ file_extension
    cv2.imwrite(outImagePath,image)


def main(path):
    imagesAvailable=os.listdir(path)
    for imagePath in imagesAvailable:
        if imagePath.endswith("png") or imagePath.endswith("jpg"):
            process(os.path.join(path,imagePath))



if __name__ == "__main__":
    pathWithImages="/home/docker/images"
    main(pathWithImages)