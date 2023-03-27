from flask import Blueprint


Form = Blueprint("form", __name__)


@Form.route("/form")
def _form():
    return "<h1> form </h1>"
