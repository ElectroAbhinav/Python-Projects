import cv2
import numpy as np

path = "Resources/Lena Headey.jpg"
Harrcascade_path = "Resources/Haarcascades/haarcascade_frontalface_default.xml"
Cersi = cv2.imread(path)

faceCascade = cv2.CascadeClassifier(Harrcascade_path)

img = cv2.resize(Cersi, (500, 600))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces =faceCascade.detectMultiScale(imgGray,1.1,4)

for(x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (250, 0, 0), 2)

cv2.imshow("Cersi Lannister", img)
cv2.imshow("Gray Lannister", imgGray)
cv2.waitKey(0)
