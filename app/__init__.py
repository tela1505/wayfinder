from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

# from config import DevConfig

# The SQLAlchemy object is defined globally
db = SQLAlchemy()
login_manager = LoginManager()


def page_not_found(e):
    return render_template('404.html'), 404


def internal_server_error(e):
    return render_template('500.html'), 500


def create_app(config_class=DevConfig):

    app = Flask(__name__)
    # Configure app wth the settings from config.py
    app.config.from_object (config_class)

    # Initialise plugins
    db.init_app (app)
    login_manager.init_app (app)

    from app.models import User, Post, Weight, Sleep, Grade
    with app.app_context():
        db.create_all()

    # Register error handlers
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)

    # Register Blueprints
    from app.main.routes import bp_main
    app.register_blueprint(bp_main)

    from app.auth.routes import bp_auth
    app.register_blueprint(bp_auth)

    from app.profile.routes import bp_prof
    app.register_blueprint(bp_prof)

    return app




