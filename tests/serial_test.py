import robotlib

def main():
  ser = robotlib.Serial()

  while 1:
    ser.write(100, 25)
    a = ser.read()
    print("got: " + a)


if __name__ == "__main__":
  main() 
