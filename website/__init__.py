from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_migrate import Migrate
db = SQLAlchemy()
migrate=Migrate(compare_type=True)
DB_NAME = "diabetesDatabase.db"




def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'DiabetesDetectionWebsite2255ss'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    migrate.init_app(app,db)

    from .home import Home
    from .auth import Auth
    from .diabetesform import Form
    from .dietandprecautions import DietAndPrecuations
    from .doctors import Doctors
    from .help import HelpUser

    app.register_blueprint(Home, url_prefix='/')
    app.register_blueprint(Auth, url_prefix='/')
    app.register_blueprint(Form, url_prefix='/')
    app.register_blueprint(DietAndPrecuations, url_prefix='/')
    app.register_blueprint(Doctors, url_prefix='/')
    app.register_blueprint(HelpUser, url_prefix='/')

    from .models import User, Patient, Doctor

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
