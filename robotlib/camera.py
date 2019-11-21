"""Wrapper class of PiCamera API

This is to make it easier to use camera specifically
for the things we need it for and not worry about all
of the extra arguments, etc. for functions.
"""
from picamera import PiCamera

class Camera:
  def __init__(self):
  	self.camera = PiCamera()
  	slef.camera.resolution = (1024, 768)

  def capture_image(self, filename):
  	self.camera.capture(filename)

  def start_recording(self, filename):
  	self.camera.start_recording(filename)

  def stop_recording(self):
  	self.camera.stop_recording()


    