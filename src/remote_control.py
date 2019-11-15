import robotlib
# why wont my import work?? :(
import time

# note: do pip install getch if you get import errors on this
import getch

if __name__ == "__main__":
	robot = robotlib.robot.Robot()
	print("Use ASWD to control the robot. Press ESC to quit...")
	while 1:
		char = getch.getch()
		if char == chr(27): #escape character
			break
		# print(char)

		if char == chr(97): #a key pressed
			print("left")
			robot.turnLeft()
			time.sleep(.300) #sleep for 300 ms
			robot.stop()

		elif char == chr(100): #d key pressed
			print("right")
			robot.turnRight()
			time.sleep(.300) #sleep for 300 ms
			robot.stop()

		elif char == chr(119): #w key pressed 
			print("forward")
			robot.forward()
			time.sleep(.300) #sleep for 300 ms
			robot.stop()

		elif char == chr(115): #s key pressed
			print("backward")
			robot.backward()
			time.sleep(.300) #sleep for 300 ms
			robot.stop()
