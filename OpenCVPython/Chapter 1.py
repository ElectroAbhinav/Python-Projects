import cv2

frameheight = 480
framewidth = 640

cap = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)
cap.set(10, 180)

while True:
    success, img = cap.read()
    cv2.imshow("Laptop Camera",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break