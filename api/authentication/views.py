from api import app
from flask import jsonify, Blueprint

auth_bp = Blueprint('auth_bp', __name__)

@app.route('/login')
def login():
    
    return jsonify({'message':'login'})
