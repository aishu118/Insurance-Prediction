from flask import Flask,render_template,request,redirect
import pickle
import numpy as np

model=pickle.load(open("charges.pkl","rb"))

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("insurance.html")

@app.route("/predict",methods=["POST"])
def predict():
    age=float(request.form.get("age"))
    sex=float(request.form.get("sex"))
    bmi=float(request.form.get("bmi"))
    children=float(request.form.get("children"))
    smoker=float(request.form.get("smoker"))
    region=float(request.form.get("region"))
    
    result=model.predict(np.array([[age,sex,bmi,children,smoker,region]]))
    return render_template('insurance.html',prediction_text='Insurance Price will be Rs. {}'.format(int(result)))


app.run(debug=True,port=5001)