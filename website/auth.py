from flask import Blueprint, render_template, request, flash


Auth = Blueprint("auth", __name__)


@Auth.route("/signup", methods=['GET', 'POST'])
def _signup():

    if request.method == 'POST':
        FirstName = request.form.get('First Name')
        LastName = request.form.get('Last Name')
        Email = request.form.get('email')
        Password = request.form.get('password1')
        Re_password = request.form.get('password2')
        City = request.form.get('city')
        Country = request.form.get('country')
        PhoneNumber = request.form.get('Phone Number')
        Gender = request.form.get('gender')

        if len(FirstName) < 2:
            flash('First name must be grater than 1 chracter', category='error')
        elif len(LastName) < 2:
            flash('Last name must be grater than 1 chracter', category='error')
        elif len(Password) < 7:
            flash('Password must be greater than 7 chracters', category='error')
        elif Password != Re_password:
            flash('The to passwords are not identical please try again',
                  category='error')
        else:
            # database will write here
            flash('account created successfully', category='success')

    return render_template("signup.html", custom_css="signup")


@Auth.route("/logout")
def _logout():
    return "<h1> logout </h1>"


@Auth.route("/login", methods=['GET', 'POST'])
def _login():

    # database needed to check if user exist or not
    return render_template("login.html",  custom_css="login")
