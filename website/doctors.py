from flask import Blueprint, render_template ,request
from flask_login import login_required, current_user
from .models import Doctor


Doctors = Blueprint("doctors", __name__)


@Doctors.route("/doctors", methods=['GET','POST'])
@login_required
def _Doctors():
 if request.method == 'POST': 
    select = request.form.get('selector')
    if select == "all":
        docdata = Doctor.query.all()
    else:
        docdata = Doctor.query.filter(Doctor.address.ilike(f'%{select}%')).all()
 else:
    docdata = Doctor.query.all()         
    
 return render_template("doctors.html", user=current_user, custom_css="doctors", data=docdata)
