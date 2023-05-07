from flask import Blueprint, render_template
from flask_login import login_required, current_user


HelpUser = Blueprint("helpuser", __name__)


@HelpUser.route("/helpuser")

def _help():
    return render_template("help.html", custom_css="help" , user = current_user)
