"""
	Upper Body Detection with Haar Cascades from OpenCV
"""
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('../cascades/haarcascade_upperbody.xml')

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
        minSize=(50, 100),
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