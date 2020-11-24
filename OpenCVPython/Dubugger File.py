import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

myColors = [#[51, 76, 74, 255, 0, 255], #detecting green color in light 2
            [39, 81, 36, 255, 107, 255], #detecting green color in light 1
            [0, 26, 154, 255, 0, 255]] #detecting red color

def findcolor(img,myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for colors in myColors:
        lower = np.array(colors[0][0:3])
        upper = np.array(colors[0][3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        cv2.imshow(str(colors[0]), mask)


while True:
    success, img = cap.read()
    findcolor(img, myColors)
    cv2.imshow("The Image", img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
