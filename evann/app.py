from PIL import Image
import base64
import re
from io import BytesIO
import os
import random
from werkzeug.utils import secure_filename
from flask import Flask, make_response, jsonify, request, redirect, url_for, flash, render_template
from model_api import ModelApi


app = Flask(__name__)

api_food = ModelApi('./models/keras_model_cookies.h5',
                    './models/labels_cookies.txt')
api_person = ModelApi('./models/keras_model_people.h5',
                        './models/labels_people.txt')

@app.route('/dish', methods=['POST'])
def dish64():
    data = request.json.get('data')
    person = request.json.get('person')
    # print(request.json)
    if not data or not person:
        return "No data"

    data = re.sub('^data:image/.+;base64,', '', data)
    image = Image.open(BytesIO(base64.b64decode(data)))

    person = re.sub('^data:image/.+;base64,', '', person)
    person_image = Image.open(BytesIO(base64.b64decode(person)))
    person_image.save("test.jpg")
    person_class = api_person.get_class_id(person_image)
    food_class = api_food.get_class_id(image)
    food_map = {
        "Green cookie": 4,
        "Blue cookie":3.5,
        "Banana": 2,
        "Noodles":8,
        "Apple": 3,
        "Background":2
    }
    return jsonify({"person": person_class,
                    "status": "Master" if person_class == "Ivan" else "PhD",
                    "food": food_class,
                    "price": food_map[food_class]})

@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)
