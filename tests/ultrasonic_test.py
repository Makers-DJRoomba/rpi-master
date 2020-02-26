import robotlib
import time

TRIG_PIN = 3
ECHO_PIN = 5

def main():
  print("setting up ultrasonic ranger...")
  ultrasonic = robotlib.ultrasonic.Ultrasonic(TRIG_PIN, ECHO_PIN)

  print("testing ultrasonic ranger...")
  while True:
    d = ultrasonic.getDistance()
    print("calculated distance = " + str(d))
    time.sleep(1)

if __name__ == "__main__":
  main()
