import cv2
import numpy as np

framWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, framWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

def empty(s):
    pass

#path = r"C:\Users\12149\Downloads\Jobs.jfif"
cv2.namedWindow("FaceBars")
cv2.resizeWindow("FaceBars",640,240)

cv2.createTrackbar("Hue Min","FaceBars",0,179,empty)
cv2.createTrackbar("Hue Max","FaceBars",179,179,empty)
cv2.createTrackbar("Sat Min","FaceBars",0,255,empty)
cv2.createTrackbar("Sat Max","FaceBars",255,255,empty)
cv2.createTrackbar("Val Min","FaceBars",0,255,empty)
cv2.createTrackbar("Val Max","FaceBars",255,255,empty)




def findSaturation(img):
    #img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "FaceBars")
    h_max = cv2.getTrackbarPos("Hue Max", "FaceBars")
    s_min = cv2.getTrackbarPos("Sat Min", "FaceBars")
    s_max = cv2.getTrackbarPos("Sat Max", "FaceBars")
    v_min = cv2.getTrackbarPos("Val Min", "FaceBars")
    v_max = cv2.getTrackbarPos("Val Max", "FaceBars")
    print(h_min, h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV,lower,upper)

    cv2.imshow("Original", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("img", mask)


while True:
    sucess, img = cap.read()
    findSaturation(img)
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break