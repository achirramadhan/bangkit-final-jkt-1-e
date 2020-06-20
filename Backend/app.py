from flask import Flask, request
from inference import Inference


inference = Inference('./cnn_do.h5')

app = Flask(__name__)

@app.route('/')
def index():
  return {"root": True}


def predict(image):
  return inference.predict(image)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)