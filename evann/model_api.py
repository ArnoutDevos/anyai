import tensorflow.keras
from PIL import Image
import numpy as np


# model = tensorflow.keras.models.load_model('./models/keras_model_cookies.h5')
class ModelApi(object):
    def __init__(self):
        self.model = tensorflow.keras.models.load_model(
            './models/keras_model_cookies.h5')

    def get_class_id(self, path):
        # Load the model
        image = Image.open(path, "r")
        # image = Image.open('./training_data/blue_cookie.png')

        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        dic = {0: 'blue cookie',
               1: 'green cookie',
               2: 'empty plate',
               3: 'background'}

        # Make sure to resize all images to 224, 224 otherwise they won't fit in the array
        image.resize((224, 224))
        image_array = np.asarray(image)[..., :3]
        normalized_image_array = image_array / 255.0
        data[0] = normalized_image_array

        # run the inference
        prediction = self.model.predict(data)
        max_pred = np.argmax(prediction)
        return dic[max_pred]
