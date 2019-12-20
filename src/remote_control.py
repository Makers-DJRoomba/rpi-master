import robotlib
import serial

# note: do pip3 install getch if you get import errors on this
import getch

def main():
	robot = robotlib.robot.Robot()
		print("Use ASWD to control the robot. Press F to stop. Use ESC to quit...")
		while 1:
			char = getch.getch()

			# ESC key pressed
			if char == chr(27):
				break

			# A key pressed
			if char == chr(97): 
				print("left")
				robot.turnLeft()

			# D key pressed
			elif char == chr(100): 
				print("right")
				robot.turnRight()

			# W key pressed 
			elif char == chr(119): 
				print("forward")
				robot.forward()

			# S key pressed
			elif char == chr(115):
				print("backward")
				robot.backward()
			
			# F key pressed
			elif char == chr(32):
				print("stop")
				robot.stop()

if __name__ == "__main__":
	main()
