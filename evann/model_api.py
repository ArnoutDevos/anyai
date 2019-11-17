import tensorflow.keras
from PIL import Image
import numpy as np


# model = tensorflow.keras.models.load_model('./models/keras_model_cookies.h5')
class ModelApi(object):
    def __init__(self, model_path, label_path):
        self.session = tensorflow.Session()
        tensorflow.keras.backend.set_session(self.session)
        init = tensorflow.global_variables_initializer()
        self.session.run(init)

        self.model = tensorflow.keras.models.load_model(
            model_path)
        self.model._make_predict_function()
        
        self.dic = self.txt_to_list(label_path)

    def txt_to_list(self, label_path):
        f = open(label_path)

        line = f.readline()
        dic = []
        while line:
            label = line.rstrip().split(' ', 1)[1]
            dic.append(label)
            line = f.readline()
        f.close()

        return dic
    
    def get_class_id(self, image):
        # Load the model
        # image = Image.open(path, "r")

        # print("opened image")
        # image = Image.open('./training_data/blue_cookie.png')

        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # Make sure to resize all images to 224, 224 otherwise they won't fit in the array
        image  = image.resize((224, 224))
        image_array = np.asarray(image)[..., :3]
        normalized_image_array = image_array / 255.0
        data[0] = normalized_image_array

        # run the inference
        print("before inference")

        with self.session.as_default():
            with self.session.graph.as_default():
                prediction = self.model.predict(data)
                max_pred = np.argmax(prediction)

        print(prediction)
        return self.dic[max_pred]
