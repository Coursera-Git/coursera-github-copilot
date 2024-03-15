from app.models.todo_model import db, Todo

def get_all_todos():
    return Todo.query.all()

def add_todo(title):
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()

def toggle_todo_complete(todo_id):
    todo = db.session.get(Todo, todo_id)
    if todo:
        todo.complete = not todo.complete
        db.session.commit()

def delete_todo(todo_id):
    Todo.query.filter_by(id=todo_id).delete()
    db.session.commit()