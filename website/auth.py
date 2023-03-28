from flask import Blueprint, render_template


Auth = Blueprint("auth", __name__)


@Auth.route("/signup")
def _signup():
    return render_template("signup.html")


@Auth.route("/logout")
def _logout():
    return "<h1> logout </h1>"


@Auth.route("/login")
def _login():
    return render_template("login.html")
