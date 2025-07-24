from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='your_secret_key',
        SQLALCHEMY_DATABASE_URI='sqlite:///app.db'
    )
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    from .routes.auth import auth as auth_blueprint
    from .routes.dashboard import dashboard as dashboard_blueprint
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(dashboard_blueprint)

    return app
