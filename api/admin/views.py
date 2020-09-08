from api import app
from flask import jsonify, Blueprint, request
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from api.models import User
from api import db

admin_bp = Blueprint('admin_bp', __name__)

@app.route('/user', methods=['GET'])
def get_all_users():
    users = User.query.all()

    output = []
    for user in users:

        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        output.append(user_data)

    return jsonify({'users': output})

@app.route('/user/<user_id>', methods=['GET'])
def get_one_user():
    return ''

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    hashed_pass = generate_password_hash(data['password'], method='sha256')
    new_user = User(
        public_id=str(uuid.uuid4()), 
        name=data['name'], 
        password=hashed_pass,
        admin=True)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message':'new user created!'})

@app.route('/user/<user_id>', methods=['PUT'])
def promote_user():
    return ''

@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user():
    return ''


