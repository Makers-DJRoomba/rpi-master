import robotlib
import serial

# note: do pip3 install getch if you get import errors on this
import getch

def main():
	ser = serial.Serial(
		port='/dev/ttyACM0',
		baudrate=9600,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS,
		timeout=1
	)

	print("Use ASWD to control the robot. Press F to stop. Use ESC to quit...")
	while 1:
		char = getch.getch()

		# ESC key pressed
		if char == chr(27): 
			break

		# A key pressed
		if char == chr(97): 
			print("left")
			ser.write(bytes('1\n'), 'utf-8')
			x = ser.readline().decode('utf-8')
			x = int(x) - 48
			print(x)

		# D key pressed
		elif char == chr(100): 
			print("right")
			ser.write(bytes('2\n'), 'utf-8')
			x = ser.readline().decode('utf-8')
			x = int(x) - 48
			print(x)

		# W key pressed 
		elif char == chr(119): 
			print("forward")
			ser.write(bytes('3\n'), 'utf-8')
			x = ser.readline().decode('utf-8')
			x = int(x) - 48
			print(x)

		# S key pressed
		elif char == chr(115): 
			print("backward")
			ser.write(bytes('4\n'), 'utf-8')
			x = ser.readline().decode('utf-8')
			x = int(x) - 48
			print(x)
		
		# F key pressed
		elif char == chr(32): 
			print("stop")
			ser.write(bytes('0'), 'utf-8')
			x = ser.readline().decode('utf-8')
			x = int(x) - 48
			print(x)

if __name__ == "__main__":
	main()
