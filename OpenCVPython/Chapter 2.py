import cv2
import numpy as np

img = cv2.imread("Resources/Spider.png")
kernel= np.ones((5,5),np.uint8)

imgray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale",imgray)

imgblur= cv2.GaussianBlur(imgray,(7,7),0)
cv2.imshow("BlurImage",imgblur)

imgcanny= cv2.Canny(img,100,100)
cv2.imshow("Canny",imgcanny)

imgdilation= cv2.dilate(imgcanny,kernel,iterations=1)
cv2.imshow("Dilated",imgdilation)

imgeroded= cv2.erode(imgdilation,kernel,iterations=5)
cv2.imshow("Eroded",imgeroded)

cv2.waitKey(0)
