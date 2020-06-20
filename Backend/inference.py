import numpy as np
import json
import tensorflow as tf

from tensorflow.keras.models import load_model
from tensorflow.image import resize
from tensorflow.image import rgb_to_grayscale
from tensorflow.keras.preprocessing.image import img_to_array


class Inference:

    # The labels in the exact order when training,
    # Please do not change this.
    labels = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]

    def __init__(self, modelpath):
        try:
            self.model = load_model(modelpath)
        except:
            print("Model not Found")
        self.inp_shape = self.model.input.shape.as_list()

    def predict(self, image):
        image = self.preprocess(image)
        preds = self.model.predict(image)
        pred = np.argmax(preds)
        return {
            "label": self.labels[pred],
            "probs": dict(zip(self.labels, preds.flatten().astype("float"))),
        }

    def preprocess(self, image):
        image = resize(
            image, (self.inp_shape[1], self.inp_shape[2])
        )  # rescale to match the input size

        # change to grayscale if the model is in grayscale
        if self.inp_shape[3] == 1 and image.shape[2] != 1:
            if image.shape[2] == 3:
                image = rgb_to_grayscale(image)
            elif image.shape[2] == 4:
                image = rgb_to_grayscale(image[:, :, :3])

        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        return image


if __name__ == "__main__":
    dummy_image = np.random.random((50, 50, 3))
    inference = Inference("./cnn_do.h5")
    print(inference.predict(dummy_image))
