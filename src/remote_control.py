import robotlib
# why wont my import work?? :(
import time
import serial

# note: do pip install getch if you get import errors on this
import getch

if __name__ == "__main__":

	ser = serial.Serial(
		port='/dev/ttyACM0',
		baudrate=9600,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS,
		timeout=1
	)
	# robot = robotlib.robot.Robot()
	print("Use ASWD to control the robot. Press ESC to quit...")
	while 1:
		char = getch.getch()
		if char == chr(27): #escape character
			break
		# print(char)

		if char == chr(97): #a key pressed
			print("left")
			# robot.turnLeft()
			ser.write(bytes('1\n'), 'utf-8')
			x = ser.readline().decode('utf-8')
			x = int(x) - 48
			print(x)
			# time.sleep(.300) #sleep for 300 ms
			# robot.stop()
			# ser.write(bytes('0'), 'utf-8')
			# x = ser.readline().decode('utf-8')
			# x = int(x) - 48
			# print(x)

		elif char == chr(100): #d key pressed
			print("right")
			# robot.turnRight()
			ser.write(bytes('2\n'), 'utf-8')
			x = ser.readline().decode('utf-8')
			x = int(x) - 48
			print(x)
			# time.sleep(.300) #sleep for 300 ms
			# robot.stop()

		elif char == chr(119): #w key pressed 
			print("forward")
			# robot.forward()
			ser.write(bytes('3\n'), 'utf-8')
			x = ser.readline().decode('utf-8')
			x = int(x) - 48
			print(x)
			# time.sleep(.300) #sleep for 300 ms
			# robot.stop()

		elif char == chr(115): #s key pressed
			print("backward")
			# robot.backward()
			ser.write(bytes('4\n'), 'utf-8')
			x = ser.readline().decode('utf-8')
			x = int(x) - 48
			print(x)
			# time.sleep(.300) #sleep for 300 ms
			# robot.stop()
		
		elif char == chr(32):
			print("stop")
			# robot.stop()
			ser.write(bytes('0'), 'utf-8')
			x = ser.readline().decode('utf-8')
			x = int(x) - 48
			print(x)
