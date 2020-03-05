#!/usr/bin/env python
import time
import serial

ser = serial.Serial(
	port='/dev/ttyACM0', 
	baudrate = 9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)
counter=0
send_data = 100
while 1:
    ser.write(bytes(str(send_data) + "," + str(send_data) + "\n", 'utf-8'))
    #ser.write('%d \n'%(counter))
    #print('Wrote: %d'%(counter))
    #print('%d'%(counter))
    print("sent: " + str(send_data))
    time.sleep(1)
    send_data -= 25
    #counter = counter % 10
    x = ser.readline().decode('utf-8')
    #x = int(x) - 48
    print("received: " + x)
