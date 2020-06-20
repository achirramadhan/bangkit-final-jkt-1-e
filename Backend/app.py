from flask import Flask, request
from inference import Inference

# initiat the inference, doing this outside any
# function as it only run once
inference = Inference('./cnn_do.h5')

app = Flask(__name__)

@app.route('/')
def index():
  return {"root": True}

# call this function for prediction or
# simply call the function inside this function
def predict(image):
  return inference.predict(image)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)