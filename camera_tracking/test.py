from picamera import PiCamera
from time import sleep
import subprocess

camera = PiCamera()
resolution = [(1024, 768), (2592, 1944)]

''' First test with taking pics '''
camera.resolution = resolution[1]
for i in range(5):
    sleep(1)
    camera.capture('/home/pi/Documents/rpi-master/camera_tracking/2592image%s.jpg' % i)
    print("took a picture")

camera.resolution = resolution[0]
for i in range(5):
    sleep(1)
    camera.capture('/home/pi/Documents/rpi-master/camera_tracking/1024image%s.jpg' % i)
    print("took a picture")

camera.resolution = resolution[1]
print("about to start recording")
sleep(1)
camera.start_recording('/home/pi/Documents/rpi-master/camera_tracking/2592video.h264')
print("started recording")
sleep(10)
camera.stop_recording()
# subprocess.run(['./mp4convert.sh'])

camera.resolution = resolution[0]
print("about to start recording")
sleep(1)
camera.start_recording('/home/pi/Documents/rpi-master/camera_tracking/1024video.h264')
print("started recording")
sleep(10)
camera.stop_recording()
# subprocess.run(['./mp4convert.sh'])

''' Next steps: process the image to find the specific object ''' 
