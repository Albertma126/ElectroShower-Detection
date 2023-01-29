# Testing web camera and Arduino with 2 LEDs
import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

cap = cv2.VideoCapture(0) # variable holding video feed
detector = FaceDetector() # adding specific features to the video feed
arduino = SerialObject("COM3")  # define arduino object

while True:
    success, img = cap.read() # img to read from cap feed
    img, bboxs = detector.findFaces(img) # adds box on face in img

    # [R, G]
    if bboxs: # if object is detected and locked, Arduino outputs GREEN
        arduino.sendData([0,1])
    else: # if no object, output RED
        arduino.sendData([1,0])

    cv2.imshow("Image", img)
    cv2.waitKey(1)
