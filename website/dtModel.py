import scipy.stats as stats
import pickle
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import zscore
import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
# import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
# %matplotlib inline

# read csv file

diabetes_data = pd.read_csv(r'C:\Users\OWNER\Music\Diabetes-prediction-system\Diabetes\diabetes_new.csv')
# show first 20 row
diabetes_data.head(20)

# check null
diabetes_data.isnull().sum()


# preprocess
diabetes_data = diabetes_data.assign(log_Age=lambda x:
                                     np.log(x['Age']))

diabetes_data = diabetes_data.assign(
    zscore_glucose=zscore(diabetes_data['PlasmaGlucose']))
diabetes_data = diabetes_data.assign(
    zscore_pressure=zscore(diabetes_data['DiastolicBloodPressure']))
diabetes_data = diabetes_data.assign(
    zscore_thick=zscore(diabetes_data['TricepsThickness']))
diabetes_data = diabetes_data.assign(
    zscore_insulin=zscore(diabetes_data['SerumInsulin']))
diabetes_data = diabetes_data.assign(zscore_bmi=zscore(diabetes_data['BMI']))

# apply min-max for other features:  pregnancy, diabetes pedigree
scaler = MinMaxScaler()

minMaxData = pd.DataFrame(scaler.fit_transform(diabetes_data.loc[:, [
                          'Pregnancies', 'DiabetesPedigree']]), columns=['minMaxPreg', 'minMaxPedigree'])
diabetes_data = pd.concat([diabetes_data, minMaxData], axis=1, join='inner')

diabetes_data.head()

# delet the coulmns that we don't need any more
diabetes_copy = diabetes_data.copy(deep=True)
del diabetes_copy['Age']
del diabetes_copy['PlasmaGlucose']
del diabetes_copy['DiastolicBloodPressure']
del diabetes_copy['TricepsThickness']
del diabetes_copy['SerumInsulin']
del diabetes_copy['BMI']
del diabetes_copy['DiabetesPedigree']
del diabetes_copy['Pregnancies']
del diabetes_copy['PatientID']

diabetes_copy.head()

# train and test

X = diabetes_copy.drop('Diabetic', axis='columns')
y = diabetes_copy.Diabetic

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=30, random_state=50)


dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)
predictions = dtree.predict(X_test)
print("Accuracy Score =", format(metrics.accuracy_score(y_test, predictions)*100))
model_train_score = dtree.score(X_train, y_train)
model_test_score = dtree.score(X_test, y_test)
print(model_train_score)
print(model_test_score)

# making .pkl file
# Firstly we will be using the dump() function to save the model using pickle
# saved_model = pickle.dumps(dtree)
pickle.dump(dtree, open("Model.pkl", "wb"))

 # Then we will be loading that saved model
model = pickle.load(open("Model.pkl", "rb"))

# # lastly, after loading that model we will use this to make predictions
model.predict(X_test)