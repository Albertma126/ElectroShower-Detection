# Testing web camera and Arduino with one LED
import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

cap = cv2.VideoCapture(1) # variable holding video feed
detector = FaceDetector() # adding specific features to the video feed
arduino = SerialObject("COM3") # define arduino object

while True:
    success, img = cap.read() # img to read from cap feed
    img, bboxs = detector.findFaces(img) # adds box on face in img

    # if object is detected and locked, Arduino outputs
    if bboxs:
        arduino.sendData([1])
    else: #do not output anything if no object
        arduino.sendData([0])

    cv2.imshow("Image", img)
    cv2.waitKey(1)
