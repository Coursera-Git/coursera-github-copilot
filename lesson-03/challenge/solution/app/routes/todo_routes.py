from flask import Blueprint, render_template, request, redirect, url_for

from app.services.todo_service import add_todo, delete_todo, get_all_todos, toggle_todo_complete

todo_bp = Blueprint('todo_bp', __name__)

@todo_bp.route('/')
def home():
    todo_list = get_all_todos()
    return render_template('base.html', todos=todo_list)


@todo_bp.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    add_todo(title)
    return redirect(url_for('todo_bp.home'))

@todo_bp.route('/toggle/<int:todo_id>')
def toggle(todo_id):
    toggle_todo_complete(todo_id)
    return redirect(url_for('todo_bp.home'))

@todo_bp.route('/delete/<int:todo_id>')
def delete(todo_id):
    delete_todo(todo_id)
    return redirect(url_for('todo_bp.home'))