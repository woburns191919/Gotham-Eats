from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_folder='../react-app/build', static_url_path='/')
    app.config.from_object(Config)
    db.init_app(app)

    login = LoginManager(app)
    login.login_view = 'auth.unauthorized'

    from app.api.user_routes import user_routes
    from app.api.auth_routes import auth_routes

    # Import home_restaurants here to avoid circular import
    from app.api.home_restaurants import home_restaurants

    app.register_blueprint(user_routes, url_prefix='/api/users')
    app.register_blueprint(auth_routes, url_prefix='/api/auth')
    app.register_blueprint(home_restaurants, url_prefix="/restaurants")

    return app
