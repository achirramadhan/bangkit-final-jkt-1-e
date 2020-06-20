import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.image import resize
from tensorflow.image import rgb_to_grayscale
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np

class Inference():
    
    labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
    
    def __init__(self, modelpath):
        try:
            self.model = load_model(modelpath)
        except:
            print("Model not Found")

        self.inp_shape = self.model.input.shape.as_list()

    def predict(self, image):
        image = self.preprocess(image)
        pred = self.model.predict(image)
        pred = np.argmax(pred)
        return self.labels[pred]

    def preprocess(self, image):
        image = resize(image, (self.inp_shape[1], self.inp_shape[2]))
        image = rgb_to_grayscale(image)
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        return image
    