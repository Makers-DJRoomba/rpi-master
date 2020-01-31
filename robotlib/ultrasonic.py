"""Class for ultrasonic sensor

Detects distance between sensor and objects in cm.
"""
import RPi.GPIO as GPIO
import time

class Ultrasonic:
  def __init__(self, trig_pin, echo_pin):
    self.trig_pin = trig_pin
    self.echo_pin = echo_pin

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(trig_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)
    GPIO.output(trig_pin, GPIO.LOW)

  def getDistance(self):
    # trigger ultrasonic sensor
    GPIO.output(self.trig_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(self.trig_pin, GPIO.LOW)

    while GPIO.input(self.echo_pin) == 0:
      start = time.time()

    while GPIO.input(self.echo_pin) == 1:
      end = time.time()

    pulse_duration_sec = end - start
    speed_of_sound     = 34300 # units: cm/s

    return pulse_duration_sec*speed_of_sound/2