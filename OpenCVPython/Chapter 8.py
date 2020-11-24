import cv2
import numpy as np
path = "Resources/Shapes.jpg"

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


def getContours( img ):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
         area = cv2.contourArea(cnt)

         if area > 500:
          print(area)

          cv2.drawContours(imgRCopy, cnt, -1, (255, 0, 0), 3)
          peri = cv2.arcLength(cnt, True)

          print(peri)

          approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
          print(len(approx))

          ObjCorner = len(approx)
          x, y, w, h = cv2.boundingRect(approx)

          if ObjCorner == 3: ObjType = "Triangle"
          elif ObjCorner == 4:
               Ratio = w/float(h)
               if Ratio >0.95 and Ratio < 1.05: ObjType = "Square"
               else: ObjType = "Rectangle"

          elif ObjCorner == 8: ObjType = "Circle"
          elif ObjCorner == 12: ObjType = "Cross"
          else: ObjType = "None"

          cv2.rectangle(imgRCopy, (x, y), (x+w, y+h), (0, 145, 165), 2)
          cv2.putText(imgRCopy, ObjType, ((x+(w//2)-10), (y+(h//2)-10)), cv2.FONT_ITALIC, 0.5, (60, 40, 70), 2)


img = cv2.imread(path)
imgR = cv2.resize(img, (320, 240))
imgRCopy = imgR.copy()
imgGray = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgBlank = np.zeros_like(imgR)
imgCanny = cv2.Canny(imgR,50,50)

getContours(imgCanny)

imgStacked = stackImages(0.8, ([imgR, imgGray, imgBlur], [imgCanny, imgRCopy, imgBlank]))

cv2.imshow("Stacked Images", imgStacked)
cv2.waitKey(0) //End of program 
