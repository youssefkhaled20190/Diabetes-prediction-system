from flask import Blueprint, render_template
from flask_login import login_required, current_user


Doctors = Blueprint("doctors", __name__)


@Doctors.route("/doctors")
@login_required
def _Doctors():
    return render_template("doctors.html", user=current_user, custom_css="doctors")
