from flask import Flask, blueprints, render_template, request, redirect, url_for, jsonify, Blueprint
from backend.image_processing import analyze_urine_strip

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/get_image', methods=['GET', 'POST'])
def get_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part in the request'}), 400

    image_file = request.files['image']

    result = analyze_urine_strip(image_file)

    return jsonify({'message': 'Image saved', 'result': result}), 200



@routes_blueprint.route('/', methods=['POST', 'GET'])
def home():
    return render_template('index.html')
