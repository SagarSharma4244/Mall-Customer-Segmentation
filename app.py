from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import os
app = Flask(__name__)

# scores = {} # scores is an empty dict already
# model = {}
# target = 'kmeans_model.pkl'
# if os.path.getsize(target) > 0:      
#     with open(target, "rb") as f:
#         unpickler = pickle.Unpickler(f)
#         # if file is not empty scores will be equal
#         # to the value unpickled
#         model = unpickler.load()

model = pickle.load(open('kmeans_model1.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        SpendingScore=float(request.form['SpendingScore'])
        AnnualIncome=int(request.form['AnnualIncome'])

        prediction=model.predict([[age,SpendingScore,AnnualIncome]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

