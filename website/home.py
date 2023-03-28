from flask import Blueprint, render_template


Home = Blueprint("home", __name__)


@Home.route("/")
def _home():
    return render_template("base.html")
