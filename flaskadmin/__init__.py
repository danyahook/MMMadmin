from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flaskadmin.config import Config

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from flaskadmin.models import Admin

    from flaskadmin.auth.routes import auth
    from flaskadmin.statistics.routes import stats
    app.register_blueprint(auth)
    app.register_blueprint(stats)

    return app
