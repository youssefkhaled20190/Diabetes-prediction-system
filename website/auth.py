from flask import Blueprint


Auth = Blueprint("auth", __name__)


@Auth.route("/signup")
def _signup():
    return "<h1>sign up </h1>"


@Auth.route("/logout")
def _logout():
    return "<h1> logout </h1>"


@Auth.route("/login")
def _login():
    return "<h1> login </h1>"
