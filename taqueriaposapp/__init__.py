from flask import Flask

# import extensions
from .extensions import db, migrate


def create_app():

    app = Flask(__name__)

    # load configuration object
    app.config.from_object('config.DevConfig')

    # import & register core blueprint
    from .core import core
    app.register_blueprint(core)

    # import & register user blueprint
    from .user import user
    app.register_blueprint(user)

    # extensions
    extensions(app)

    return app


def extensions(app):
    """
    Initialize extensions
    """
    db.init_app(app)
    migrate.init_app(app, db)
