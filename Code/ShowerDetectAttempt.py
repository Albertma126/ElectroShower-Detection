# Attempt 1
# This program is definitely inherently flawed and will be far from our expectations
import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0) # variable holding video feed
cap.set(3, frameWidth)
cap.set(4, frameHeight)

detector = FaceDetector() # adding specific features to the video feed
arduino = SerialObject("COM3")  # define arduino object

greaseHSV = [[4, 179, 33, 100, 63, 255],
          [133, 159, 20, 87, 0, 255],
          [18, 32, 95, 207, 95, 255]]  # holds values to match objects with grease


while True:
    success, img = cap.read() # img to read from cap feed
    img, bboxs = detector.findFaces(img) # adds box on face in img

    # [R, G]
    if bboxs: # if object is detected and locked, Arduino outputs GREEN
        arduino.sendData([0,1])
    else: # if no object detected, output RED
        arduino.sendData([1,0])

    cv2.imshow("Image", img)
    cv2.waitKey(1)