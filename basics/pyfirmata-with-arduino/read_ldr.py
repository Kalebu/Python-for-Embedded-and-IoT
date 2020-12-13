
import time
from pyfirmata import Arduino, util

board = Arduino('/dev/ttyUSB0')

util.Iterator(board).start()
board.analog[0].enable_reporting()

while True:
  light_intensity = board.analog[0].read()
  print(light_intensity)
  time.sleep(0.1)
