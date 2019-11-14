"""
	Face Detection with Haar Cascades from OpenCV
	Run with second argument as filepath of pre-trained face classifiers
"""
import numpy as np
import sys
import cv2

#my local path hehe just so i remember
#/usr/local/Cellar/opencv/4.1.2/share/opencv4/lbpcascades/lbpcascade_frontalface.xml
cascade_path = sys.argv[1]
face_cascade = cv2.CascadeClassifier(cascade_path)

#start video
video_capture = cv2.VideoCapture(0)
cv2.namedWindow('video_frame', cv2.WINDOW_NORMAL)

while True:
    #capture by frame
    ret, frame = video_capture.read()

    #most classifiers are gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    #draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #show video
    cv2.imshow('video_frame', frame)

    #quit program by pressing q on video window
    if cv2.waitKey(20) & 0xFF == ord('q'):
    	break

#release when done
video_capture.release()
cv2.destroyAllWindows()