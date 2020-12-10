from flask import Flask

# import extensions
from .extensions import db, migrate


def create_app():

    app = Flask(__name__)

    # load configuration object
    app.config.from_object('config.DevConfig')

    # import & register core blueprint
    from .core import core as core_bp
    app.register_blueprint(core_bp)

    # extensions
    extensions(app)

    return app


def extensions(app):
    """
    Initialize extensions
    """
    db.init_app(app)
    migrate.init_app(app, db)
    pass
