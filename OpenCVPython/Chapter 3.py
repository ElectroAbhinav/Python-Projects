import cv2
import numpy as np

img= cv2.imread("Resources/Agera.png")
print(img.shape)

imgresize= cv2.resize(img,(300,200))
print(imgresize.shape)
imgcropped= img[0:300,400:600]

#cv2.imshow("Default",img)
#cv2.imshow("Resized",imgresize)
cv2.imshow("Cropped",imgcropped)

cv2.waitKey(0)