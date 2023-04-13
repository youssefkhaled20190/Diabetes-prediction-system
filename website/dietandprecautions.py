from flask import Blueprint, render_template
from flask_login import login_required, current_user


DietAndPrecuations = Blueprint("dietandprecautions", __name__)


@DietAndPrecuations.route("/dietandprecautions")
@login_required
def _DietAndPrecuations():
    return render_template("diet.html", user=current_user, custom_css="diet")
