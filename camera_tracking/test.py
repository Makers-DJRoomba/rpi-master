from picamera import PiCamera
from time import sleep

camera = PiCamera()

''' First test with taking pics '''
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
    print("took a picture")

''' Record video for 5 seconds and save '''
camera.start_recording('/home/pi/Desktop/video.h264')
print("started recording")
sleep(5)
camera.stop_recording()

''' Next steps: process the image to find the specific object ''' 
