from flask import Blueprint


Home = Blueprint("home", __name__)


@Home.route("/")
def _home():
    return "<h1> home </h1>"
