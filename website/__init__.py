from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'DiabetesDetectionWebsite2255ss'

    from .home import Home
    from .auth import Auth
    from .diabetesform import Form

    app.register_blueprint(Home, url_prefix='/')
    app.register_blueprint(Auth, url_prefix='/')
    app.register_blueprint(Form, url_prefix='/')

    return app
