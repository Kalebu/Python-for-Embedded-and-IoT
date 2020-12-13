import time  
from serial import Serial

arduino = Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)

def blink():
  while True:
    arduino.write(b'o')
    time.sleep(1)
    arduino.write(b'f')
    time.sleep(1)

blink()