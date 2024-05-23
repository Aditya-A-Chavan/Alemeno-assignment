from flask import Flask, blueprints, render_template, request, redirect, url_for, jsonify, Blueprint

routes_blueprint = Blueprint('routes', __name__)

routes_blueprint.route('/get_image', methods=['GET'])
def get_image():
    return 0

routes_blueprint.route('/', methods=['POST', 'GET'])
def home():
    return render_template('index.html')
