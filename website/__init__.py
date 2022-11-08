from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
basedir = path.abspath(path.dirname(__file__))
DB_NAME = 'filmoteka.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sdfafeqfawaqq'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        path.join(basedir, DB_NAME)
    db.init_app(app)

    from .controllers.auth import auth
    from .controllers.sreview import sreview
    from .controllers.games import games
    from .controllers.movies import movies

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(sreview, url_prefix='/')
    app.register_blueprint(games, url_prefix='/games')
    app.register_blueprint(movies, url_prefix='/movies')

    from .models import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.sign_in'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return (User.query.get(int(id)))

    return app
