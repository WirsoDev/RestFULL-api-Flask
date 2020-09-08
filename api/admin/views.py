from api import app
from flask import jsonify, Blueprint

admin_bp = Blueprint('admin_bp', __name__)

@app.route('/admin')
def admin():
    return jsonify({'message':'hello World'})
