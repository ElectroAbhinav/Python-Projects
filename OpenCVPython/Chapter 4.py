import cv2
import numpy as np

img= np.zeros((512,512,3), np.uint8)
#print(img)
#img[]=255,0,0

cv2.line(img,(0,0),(250,350),(0,255,0))
cv2.rectangle(img,(0,0),(250,350),(0,0,300),2)
cv2.circle(img,(250,350),100,(200,100,150),50)
cv2.putText(img,"This is OpenCV Intro",(60,60),cv2.FONT_ITALIC,1,(400,300,500),3)

cv2.imshow("Object",img)

cv2.waitKey(0)