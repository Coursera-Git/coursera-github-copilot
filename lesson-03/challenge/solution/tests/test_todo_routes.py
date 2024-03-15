import unittest
from app import create_app
from app.models.todo_model import db, Todo

app = create_app()


class TestApp(unittest.TestCase):

    # Set up the testing environment
    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        with app.app_context():
            db.create_all()

    # Tear down the testing environment
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # Test the home route
    def test_home_route(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)

    # Test the add route
    def test_add_route(self):
        with app.test_client() as client:
            response = client.post('/add', data=dict(title='Test Todo'))
            self.assertEqual(response.status_code, 302)  # Redirect status code

    # Test the update route
    def test_update_route(self):
        with app.app_context():
            # Add a todo for testing
            todo = Todo(title='Test Todo', complete=False)
            db.session.add(todo)
            db.session.commit()

        with app.test_client() as client:
            response = client.get('/toggle/1')
            self.assertEqual(response.status_code, 302)  # Redirect status code
            updated_todo = db.session.get(Todo, 1)  # Use Session.get() instead of Todo.query.get()
            self.assertEqual(updated_todo.complete, True)  # Check if todo was updated

    # Test the delete route
    def test_delete_route(self):
        with app.app_context():
            # Add a todo for testing
            todo = Todo(title='Test Todo', complete=False)
            db.session.add(todo)
            db.session.commit()

        with app.test_client() as client:
            response = client.get('/delete/1')
            self.assertEqual(response.status_code, 302)  # Redirect status code
            deleted_todo = db.session.get(Todo, 1)  # Use Session.get() instead of Todo.query.get()
            self.assertIsNone(deleted_todo)  # Check if todo was deleted

if __name__ == '__main__':
    unittest.main()
