from flask import Blueprint, render_template
from flask_login import login_required, current_user


Form = Blueprint("form", __name__)


@Form.route("/form")
@login_required
def _form():
    return render_template("form.html", user=current_user, custom_css="form")
