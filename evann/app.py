import os
import random
from werkzeug.utils import secure_filename
from flask import Flask, make_response, jsonify, request, redirect, url_for, flash, render_template
from model_api import ModelApi


app = Flask(__name__)

api = ModelApi()


@app.route('/dish', methods=['POST'])
def dish():

    if 'image' not in request.files:
        return "No file"
    image = request.files['image']

    if not image:
        return "No file"

    image.save("test.png")

    return jsonify({"class": api.get_class_id("test.png")})


def get_class_ida(a):
    return 0


@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)
