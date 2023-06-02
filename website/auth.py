from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

Auth = Blueprint("auth", __name__)


@Auth.route("/signup", methods=['GET', 'POST'])
def _signup(): 


    if request.method == 'POST':
        FirstName = request.form.get('First Name')
        LastName = request.form.get('Last Name')
        Email = request.form.get('email')
        Password = request.form.get('password1')
        Re_password = request.form.get('password2')
        City = request.form.get('City')
        Country = request.form.get('Country')
        PhoneNumber = request.form.get('Phone Number')
        Gender = request.form.get('gender')

        user = User.query.filter_by(email=Email).first()
        if user:
            flash('user already exist !', category="error")
        elif len(FirstName) < 2:
            flash('First name must be grater than 1 chracter', category='error')
        elif len(LastName) < 2:
            flash('Last name must be grater than 1 chracter', category='error')
        elif len(Password) < 7:
            flash('Password must be greater than 7 chracters', category='error')
        elif Password != Re_password:
            flash('The to passwords are not identical please try again',
                  category='error')
        else:
            New_User = User(email=Email, password=generate_password_hash(Password, method='sha256'), first_name=FirstName, last_name=LastName,
                            city=City, country=Country, phone_number=PhoneNumber, gender=Gender)
            db.session.add(New_User)
            db.session.commit()
            login_user(New_User, remember=True)
            db.session.close_all()
            flash('account created successfully', category='success')
            return redirect(url_for('auth._login'))

    return render_template("signup.html", custom_css="signup", user=current_user)


@Auth.route("/logout")
@login_required
def _logout():
    logout_user()
    return redirect(url_for('auth._login'))


@Auth.route("/login", methods=['GET', 'POST'])
def _login():

    if request.method == 'POST':
        Email = request.form.get('email')
        Password = request.form.get('password')

        user = User.query.filter_by(email=Email).first()

        if user:
            if check_password_hash(user.password, Password):
                flash('Logging in successfully!', category="success")
                login_user(user, remember=True)
                return redirect(url_for('home._home'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash("email doesn't exist", category='error')

    return render_template("login.html",  custom_css="login", user=current_user)
