from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from .config import Config
from .auth import auth

login_manager = LoginManager()
login_manager.login_view = 'auth.login'



def create_app():
    app = Flask(__name__, template_folder='./templates', static_folder='./static')
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)

    # login_manager.init_app(app)

    app.register_blueprint(auth)

    return app
    