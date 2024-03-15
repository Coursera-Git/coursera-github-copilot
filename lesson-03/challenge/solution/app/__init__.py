from flask import Flask
from app.models.todo_model import db
from app.routes.todo_routes import todo_bp
import config

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config.Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()  

    app.register_blueprint(todo_bp)

    return app