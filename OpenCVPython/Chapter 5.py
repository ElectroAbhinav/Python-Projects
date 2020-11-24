import cv2
import numpy as np
img= cv2.imread("Resources/Cards.png")
width,heigth= 275,475

pts1= np.float32([[66,275],[39,380],[288,379],[300,338]])
pts2= np.float32([[0,0],[width,0],[0,heigth],[width,heigth]])

matrix= cv2.getPerspectiveTransform(pts1,pts2)
imgOutput= cv2.warpPerspective(img,matrix,(width,heigth))


cv2.imshow("Art",img)
cv2.imshow("WarpImage",imgOutput)

cv2.waitKey(0)