from flask import Flask
from Arduino import Arduino

board = Arduino()
app = Flask(__name__)

board.pinMode(13, "OUTPUT")

@app.route('/<command>')
def Gateway(command):
    if str(command) == 'on':
        board.digitalWrite(13, "HIGH")
        response = "The led is on"
    elif str(command) == 'off':
        board.digitalWrite(13, "LOW")
        response = "The led is off"
    else:
        response = 'Uknown command'
    return {'response': response}

if __name__ == '__main__':
  app.run(debug=True)
