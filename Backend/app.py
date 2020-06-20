import numpy as np
import io
import tensorflow as tf

from flask import Flask, request, send_file
from inference import Inference


# initiat the inference, doing this outside any
# function as it only run once
inference = Inference("./cnn_do.h5")

app = Flask(__name__)


@app.route("/")
def index():
    return {"root": True}


# call this function for prediction or
# simply call the function inside this function
def predict(image):
    return inference.predict(image)


@app.route("/predict", methods=["POST"])
def get_prediction():
    image = request.files["image"]

    in_memory_file = io.BytesIO()
    image.save(in_memory_file)

    tf_image = tf.io.decode_image(in_memory_file.getvalue())
    result = predict(tf_image)
    return {"result": result}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

