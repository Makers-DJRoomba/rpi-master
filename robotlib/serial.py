"""Class for serial I2C communication with microcontroller

Sends/Receives raw data over serial bus to microcontroller.
"""
import serial

class Serial:
  
  def __init__(self):
    self.ser = = serial.Serial(
        port='/dev/ttyACM0', 
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

  #write to serial with data
  def write(self, data):
    self.ser.write('%d\n'%(data))
    print('sent: ' + data)

  #keep reading until value is received, then return 
  def read(self):
    received = self.ser.readline()

    while(not received):
      received = self.ser.readline()

    print('recieved: ' + received)
    received_int = int(received) - 48
    return received_int

  def close(self):
    self.ser.close()

