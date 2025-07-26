from flask import Flash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

def create_app():
    app = Flash(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    db.init_app(app)
    return app