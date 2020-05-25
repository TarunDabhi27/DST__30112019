import pandas as pd
import numpy as np
from flask import Flask,request
import pickle

regression_model = pickle.load(open('./RegressionModel.pkl','rb'))


app = Flask(__name__)

@app.route("/getPremium")
def predictPremium():
    age = request.args.get('age',type=int)
    bmi = request.args.get('bmi', type=int)
    children = request.args.get('children', type=int)
    gender = request.args.get('gender')
    smoker = request.args.get('smoker')
    region = request.args.get('region')
    insurance = pd.DataFrame([[age,bmi,children,gender,smoker,region]],columns=['age','bmi','children','gender','smoker','region'])
    insurance = pd.get_dummies(insurance)
    missing_col = set(['const', 'age', 'bmi', 'children', 'gender_female', 'gender_male', 'smoker_no', 'smoker_occasionally', 'smoker_yes', 'region_northeast', 'region_northwest', 'region_southeast', 'region_southwest']) - set(insurance.columns)
    for col_name in missing_col:
        insurance[col_name]=0
    print(insurance)
    predicted_premium = regression_model.predict(insurance)
    return str(predicted_premium[0])

if __name__=="__main__":
    app.run(debug=True)