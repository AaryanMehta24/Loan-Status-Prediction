
import numpy as np
from flask import Flask, jsonify, render_template,request
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def main():
    return render_template('index.html')

# @app.route('/predict',methods=['POST'])
# def predict():
    int_features

@app.route('/predict',methods=['POST','GET'])
def predict():
    print(request.form)
    int_features = [int(x) for x in request.form.values()]
    age = int_features[0]
    age=int(age)
    int_features.pop(0)
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    prediction = model.predict(final)
    output= prediction

    # int_features = final.reshape(1,-1)

    #Standarize the input data
    # scaler = StandardScaler()
    # scaler.fit(final)
    # std_data = scaler.transform(final)
    # print(std_data)

    # prediction = model.predict(std_data)
    # print(prediction)
    if age<18:
        return render_template('index.html',age_text='Age is less than 18')
    if age>60:
        return render_template('index.html',age_text='Age is greater than 60')


    if (output[0] == 0):
        print("Loan is Not Approved")
    else:
        print("Loan is Approved")

    # gender = request.form.values['Gender']
    # marital = request.form.values['Marital']
    # dependents = request.form.values['Dependents']
    # education = request.form.values['Education']
    # employed = request.form.values['Employed']
    # income = request.form.values['Income']
    # coappincome = request.form.values['CoappIncome']
    # loanamount = request.form.values['loanAmt']
    # term = request.form.values['Term']
    # history = request.form.values['History']
    # propertyType = request.form.values['Property']
    # arr = np.array([[gender,marital,dependents,education,employed,income,coappincome,loanamount,term,history,propertyType]])
    # prediction = model.predict(arr)
    # pred = model.predict(arr)
    # output = prediction[0]
    # print(output[0])
    
    if prediction[0] == 1:
        print('Loan Approved')
        return render_template('index.html',prediction_text='Loan is Approved')
    else:
        print("loan not Approved")
        return render_template('index.html',prediction_text='Loan is not Approved')

    # print(arr)



if __name__ == "__main__":
    app.run(debug=True)