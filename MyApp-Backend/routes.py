# routes.py

from flask import request, jsonify
from models import TodoItem, db

@app.route('/api/add_todo', methods=['POST'])
def add_todo():
    todo_data = request.get_json()
    title = todo_data.get('title')

    if not title:
        return jsonify({'error': 'Title is required.'}), 400

    new_todo = TodoItem(title=title)
    db.session.add(new_todo)
    db.session.commit()

    return jsonify({'message': 'Todo item added successfully.', 'todo_id': new_todo.id}), 200
