import os
import random
from werkzeug.utils import secure_filename
from flask import Flask, make_response, jsonify, request, redirect, url_for, flash, render_template
from model_api import ModelApi


app = Flask(__name__)

api = ModelApi()


@app.route('/dish', methods=['POST'])
def dish():

    if 'food' not in request.files:
        return "No file"
    image = request.files['food']

    if not image:
        return "No file"

    image.save("test.png")

    return jsonify({"person": "arnout",
                    "status": "PhD",
                    "food": api.get_class_id("test.png"),
                    "price": 11.50})

def get_class_ida(a):
    return 0


@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)
