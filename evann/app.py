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

api = ModelApi()


@app.route('/dish', methods=['POST'])
def dish64():
    data = request.form.get('data')
    print(request.form)
    if not data:
        return "No data"

    data = re.sub('^data:image/.+;base64,', '', data)
    image = Image.open(BytesIO(base64.b64decode(data)))
    image.save("test.png")

    return jsonify({"person": "arnout",
                    "status": "PhD",
                    "food": api.get_class_id("test.png"),
                    "price": 11.50})

@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)
