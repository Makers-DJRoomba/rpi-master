"""Class for basic robot control

Class takes motion commands and sends 
them over I2C to microcontroller.
"""
from .i2c import I2C

class Robot:
  def __init__(self):

  # can make separate rotateLeft/Right functions if helpful
  def turnLeft(self):
    # implement as I2C command

  def turnRight(self):
    # implement as I2C command

  def forward(self):
    # implement as I2C command

  def backward(self):
    # implement as I2C command

  def stop(self):   
    # implement as I2C command
