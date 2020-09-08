from flask import jsonify, request
from api import app
from functools import wraps
import jwt
from api.models import User 

def token_requiered(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message':'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message':'tokan is not valid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated