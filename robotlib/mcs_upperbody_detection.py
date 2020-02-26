"""
	MCS Upper Body Detection with Haar Cascades from OpenCV
"""
import numpy as np
import cv2
import time
import imutils
from imutils.video import VideoStream
import signal
import sys

body_cascade = cv2.CascadeClassifier('../cascades/haarcascade_mcs_upperbody.xml')

#start video
vs = VideoStream(usePiCamera=True).start()

time.sleep(2.0)

while True:
    #capture by frame
    frame = vs.read()

    #most classifiers are gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect bodies
    bodies = body_cascade.detectMultiScale(
        gray,
        scaleFactor=1.01,
        minNeighbors=5,
        minSize=(50, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    #draw rectangles around bodies
    if(len(bodies) > 0):
          (x, y, w, h) = bodies[0]
          print("object found at " + str((x+w)/2) + ", " + str((y+h)/2))
    else:
          print("nothing detected")

