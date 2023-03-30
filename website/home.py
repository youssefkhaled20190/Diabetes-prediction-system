from flask import Blueprint, render_template
from flask_login import login_required, current_user


Home = Blueprint("home", __name__)


@Home.route("/")
def _home():
    return render_template("home.html", custom_css="home", user=current_user)
