import robotlib

TRIG_PIN = 1
ECHO_PIN = 2

def main():
  print("setting up ultrasonic ranger...")
  ultrasonic = Ultrasonic(TRIG_PIN, ECHO_PIN)

  print("testing ultrasonic ranger...")
  while True:
    d = ultrasonic.getDistance()
    print("calculated distance = " + str(d))

if __name__ == "__main__":
  main()