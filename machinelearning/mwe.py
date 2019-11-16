import tensorflow.keras
from PIL import Image
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('./models/keras_model_cookies.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image = Image.open('./training_data/blue_cookie.png')

dic = {0: 'blue cookie',
        1: 'green cookie',
        2: 'empty plate',
        3: 'background'}

# Make sure to resize all images to 224, 224 otherwise they won't fit in the array
image.resize((224, 224))
image_array = np.asarray(image)[...,:3]

# Normalize the image
normalized_image_array = image_array / 255.0

# Load the image into the array
data[0] = normalized_image_array

# run the inference
prediction = model.predict(data)
max_pred = np.argmax(prediction)
print(dic[max_pred])