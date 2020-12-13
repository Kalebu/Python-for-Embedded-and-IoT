import time
from Arduino import Arduino

board = Arduino()

while True:
    light_intensity = board.analogRead(0)
    print(light_intensity)
    time.sleep(0.1)
