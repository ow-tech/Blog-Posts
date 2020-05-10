from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db= SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'main.login'

# Initializing application
def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    #Initializing flask extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)


    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

     # setting config
    # from .requests import configure_request
    # configure_request(app)


    return app