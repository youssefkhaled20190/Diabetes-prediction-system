from flask import Blueprint, render_template,request , redirect , url_for, flash
import pandas as pd
import numpy as np
from flask_login import login_required, current_user
import pickle
import time 

Form = Blueprint("form", __name__)

#define constants to use them in mathematical operations
PlasmaGlucoseMEAN=107.85686666666666
PlasmaGlucoseSTD=31.98197465181089
DiastolicBloodPressureMEAN=71.22066666666667
DiastolicBloodPressureSTD=16.758716036531574
TricepsThicknessMEAN=28.814
TricepsThicknessSTD=14.555715781922968
SerumInsulinMEAN=137.85213333333334
SerumInsulinSTD=133.06825195901257
BMIMEAN=31.509646041017334
BMISTD=9.758999734051898
PregnanciesMIN =  0
PregnanciesMAX =  14
DiabetesPedigreeMIN =  0.078043795
DiabetesPedigreeMAX =  2.301594189

#load the model.pkl
model=pickle.load(open(r'Model.pkl','rb'))
#---------------end-----------------

@Form.route("/form",methods=['GET',"POST"])
@login_required
def _form():
    
  if request.method == 'POST':
    glucose=request.form.get("Glucose")
    bloodPressure=request.form.get("Blood-pressure")
    skinThickness=request.form.get("Skin-Thickness")
    insulin=request.form.get("Insulin-Level")
    bmi=request.form.get("bmi")
    pregnancies=request.form.get("Pregnancies")
    pedigree=request.form.get("diabetes-function")
    age=request.form.get("age")
    
    if not pregnancies:
      flash("please enter valid value",category='error')
    
    elif not glucose:
      flash("please enter valid value",category='error')
    elif not bloodPressure:
      flash("please enter valid value",category='error')
    
    elif not bmi:
      flash("please enter valid value",category='error')
    elif not age:
      flash("please enter valid value",category='error')
    
    else:
      if not skinThickness and not insulin and not pedigree:
        skinThickness=18
        insulin=20
        pedigree=0.879
        print(insulin,pedigree,skinThickness)
      elif not skinThickness and not insulin:
        skinThickness=18
        insulin=20
      elif not skinThickness and not pedigree:
        skinThickness=18
        pedigree=0.879
        
        print(pedigree,skinThickness)
      elif not insulin and not pedigree:
        insulin=20
        pedigree=0.879
        
        print(pedigree,insulin)
      elif not skinThickness:
        skinThickness=18
      
        print(skinThickness)
      elif not insulin:
        insulin=20
      
        print(insulin)
      elif not pedigree:
        pedigree=0.879
      
        print(pedigree)
        
        
      PlasmaGlucoseZscore=(float(glucose)-PlasmaGlucoseMEAN)/PlasmaGlucoseSTD
      DiastolicBloodPressureZscore=(float(bloodPressure)-DiastolicBloodPressureMEAN)/DiastolicBloodPressureSTD
      TricepsThicknessZscore=(float(skinThickness)-TricepsThicknessMEAN)/TricepsThicknessSTD
      SerumInsulinZscore=(float(insulin)-SerumInsulinMEAN)/SerumInsulinSTD
      BMIZscore=(float(bmi)-BMIMEAN)/BMISTD
      Pregnancies_scaled=(float(pregnancies)-PregnanciesMIN)/(PregnanciesMAX-PregnanciesMIN)
      DiabetesPedigree_scaled=(float(pedigree)-DiabetesPedigreeMIN)/(DiabetesPedigreeMAX-DiabetesPedigreeMIN)
      logAge = np.log(float(age))
    
    
      features=pd.DataFrame([{"log_Age":logAge , "zscore_glucose":PlasmaGlucoseZscore , "zscore_pressure":DiastolicBloodPressureZscore ,"zscore_thick": TricepsThicknessZscore ,"zscore_insulin": SerumInsulinZscore ,
                     
                 "zscore_bmi": BMIZscore ,"minMaxPreg": Pregnancies_scaled ,"minMaxPedigree": DiabetesPedigree_scaled   }])
      prediction=model.predict(features) 
      
      
      print("test")
      print(prediction)
    
      if prediction[0]==0:
        return render_template("result.html"  , user=current_user , msg = "Negative" , custom_css="result" , res=0)
      elif prediction[0]==1:
        return render_template("result.html"  , user=current_user , msg = "positive" , custom_css="result" , res=1)
      
    
    
    
    
    
    
     
     
      #check if the user dont't know the value of pedigree function,skin thickness and insulin level ,then give a default value for them 
    # else:
    #   skinThickness== None and insulin==None and pedigree==None:
    #   PlasmaGlucoseZscore=(glucose-PlasmaGlucoseMEAN)/PlasmaGlucoseSTD
    #   DiastolicBloodPressureZscore=(bloodPressure-DiastolicBloodPressureMEAN)/DiastolicBloodPressureSTD
    #   TricepsThicknessZscore=(20.00-TricepsThicknessMEAN)/TricepsThicknessSTD
    #   SerumInsulinZscore=(17-SerumInsulinMEAN)/SerumInsulinSTD
    #   BMIZscore=(bmi-BMIMEAN)/BMISTD
    #   Pregnancies_scaled=(pregnancies-PregnanciesMIN)/(PregnanciesMAX-PregnanciesMIN)
    #   DiabetesPedigree_scaled=(0.879-DiabetesPedigreeMIN)/(DiabetesPedigreeMAX-DiabetesPedigreeMIN)
    #   logAge = np.log(age)
    
    #   features=pd.DataFrame([{"log_Age":logAge , "zscore_glucose":PlasmaGlucoseZscore , "zscore_pressure":DiastolicBloodPressureZscore ,"zscore_thick": TricepsThicknessZscore ,"zscore_insulin": SerumInsulinZscore ,
                     
    #              "zscore_bmi": BMIZscore ,"minMaxPreg": Pregnancies_scaled ,"minMaxPedigree": DiabetesPedigree_scaled   }])
    #   prediction=model.predict(features) 
         
    
    
    
    
      
    
  
  return render_template("form.html", user=current_user, custom_css="form",)
    
