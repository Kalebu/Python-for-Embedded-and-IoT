from Arduino import Arduino
from ghost import ghost_ear

board = Arduino()

def check_outside():
    for _ in range(1000):
        intensity = board.analogRead(0)
    intensity = board.analogRead(0)
    return intensity


def Eve_Soul():
    while True:
        print(board.analogRead(0))
        something = ghost_ear.listen()
        if something:
            outside_combo = ['outside', 'light', 'how', 'is outside', 'how is']
            if any(word for word in something.split() if word in outside_combo):
                outside = check_outside()
                print('outside intensity ', outside)
                if outside > 0:
                    print('It\'s not that dark')
                    board.digitalWrite(13, 'LOW')
                    continue
                print('Outside is dark, I\'m switching light on')
                board.digitalWrite(13, "HIGH")
                continue
            print('It\'s great serving you what can I help?')
            
if __name__ == "__main__":
    Eve_Soul()

    
