from flask import Flask
app = Flask(__name__)


@app.route('/')
def Gateway():
  return {
      'who_am_i': 'I\'m a very simple IoT Gateway'
  }


if __name__ == '__main__':
  app.run(debug=True)
