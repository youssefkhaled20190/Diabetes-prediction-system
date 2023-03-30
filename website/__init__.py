from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db=SQLAlchemy()
DB_NAME="diabetesDatabase.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'DiabetesDetectionWebsite2255ss'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .home import Home
    from .auth import Auth
    from .diabetesform import Form

    app.register_blueprint(Home, url_prefix='/')
    app.register_blueprint(Auth, url_prefix='/')
    app.register_blueprint(Form, url_prefix='/')
    
    
    
    with app.app_context():
        db.create_all()

    return app
