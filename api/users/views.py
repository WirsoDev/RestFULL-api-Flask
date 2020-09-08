from api import app
from flask import jsonify, Blueprint

users_bp = Blueprint('users_bp', __name__)

@app.route('/')
def index():
    return jsonify({'message':'index'})

@app.route('/users')
def user():
    return jsonify({'message':'hello user'})
