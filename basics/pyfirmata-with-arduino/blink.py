import time
from pyfirmata import Arduino

board = Arduino('/dev/ttyUSB0')


def blink():
  while True:
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)


blink()
