from flask import Blueprint, render_template, request


Auth = Blueprint("auth", __name__)


@Auth.route("/signup", methods=['GET', 'POST'])
def _signup():

    if request.method == 'POST':
        FirstName = request.form.get('firstname')
        LastName = request.form.get('lastname')
        Email = request.form.get('email')
        Password = request.form.get('password1')
        Re_password = request.form.get('password2')
        City = request.form.get('city')
        Country = request.form.get('country')
        PhoneNumber = request.form.get('phonenumber')
        Gender = request.form.get('gender')

    return render_template("signup.html", custom_css="signup")


@Auth.route("/logout")
def _logout():
    return "<h1> logout </h1>"


@Auth.route("/login", methods=['GET', 'POST'])
def _login():
    return render_template("login.html",  custom_css="login")
