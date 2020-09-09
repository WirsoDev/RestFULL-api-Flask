from api import app, db
from flask import jsonify, Blueprint, request
from api.models import Todo
from api.authentication.token_required import token_requiered

users_bp = Blueprint('users_bp', __name__)

@app.route('/todo', methods=['GET'])
@token_requiered
def get_all_todos(current_user):

    if not current_user.admin:
        return jsonify({'message':'Cannot perform that function!'})

    todos = Todo.query.all()
    output = []

    for todo in todos:
        data = {}
        data['text'] = todo.text
        data['complete'] = todo.complete
        data['user_id'] = todo.user_id
        output.append(data)

    return jsonify({'todos': output})


@app.route('/todos/<todo_id>', methods=['GET'])
@token_requiered
def get_one_todo(current_user, todo_id):

    todo = todos.
    return ''


@app.route('/todo', methods=['POST'])
@token_requiered
def create_todo(current_user):
    data = request.get_json()

    new_todo = Todo(text=data['text'], complete=False, user_id=current_user.id)
    db.session.add(new_todo)
    db.session.commit()

    return jsonify({'message':'New todo created!'})


@app.route('/todo/<todo_id>', methods=['PUT'])
@token_requiered
def complete_todo(current_user, todo_id):
    return ''


@app.route('/todo/<todo_id>', methods=['DELETE'])
@token_requiered
def delete_todo(current_user, todo_id):
    return ''


