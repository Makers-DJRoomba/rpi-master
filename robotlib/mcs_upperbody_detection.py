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
# video_capture = cv2.VideoCapture(0)
# cv2.namedWindow('video_frame', cv2.WINDOW_NORMAL)
vs = VideoStream(usePiCamera=True).start()


time.sleep(0.1)

while True:
    #capture by frame
    # ret, frame = video_capture.read()
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
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        break

    #show video
    cv2.imshow('video_frame', frame)
    cv2.waitKey(1)

    #quit program by pressing q on video window
    signal.signal(signal.SIGINT, signal_handler)
    # if cv2.waitKey(20) & 0xFF == ord('q'):
    	# break

#release when done
def signal_handler:
    sys.exit()
    # video_capture.release()
    # cv2.destroyAllWindows()