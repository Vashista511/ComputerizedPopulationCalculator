import array
import numpy as np
from flask import Flask,request,jsonify,render_template,session,redirect
import pyrebase
import pickle
from sklearn import *
from sklearn.preprocessing import PolynomialFeatures
#create flask app
app = Flask(__name__)
config = {
  "apiKey": "AIzaSyBqbJxj3dubD-n8rIr8oSJrNgsYinWGQdk",
  "authDomain": "softwareengineering-a35b6.firebaseapp.com",
  "projectId": "softwareengineering-a35b6",
  "storageBucket": "softwareengineering-a35b6.appspot.com",
  "messagingSenderId": "449785318210",
  "appId": "1:449785318210:web:f3b05bddcd80f97e6456db",
  "measurementId": "G-YJSFGPZ7PZ",
  "databaseURL": " "
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
# auth.create_user_with_email_and_password('rohinjoshi@gmail.com','qwertyu')
#Load pickle model
model = pickle.load(open("model.pkl","rb"))
fits = pickle.load(open("poly.pkl","rb"))
app_secret = 'happy_flow'
@app.route("/",methods=['POST','GET'])
def index():
    if ('user' in session):
        return "Hi {}".format(session['user'])
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # print(email,password)
        try:
            user = auth.sign_in_with_email_and_password(email=email,password=password)
            session[user] = email
            print(user)
            return redirect('/home')
        except Exception as e:
           return redirect("/home")
    return render_template("login.html")

# @app.route("/logout")
# def logout()

@app.route("/home")
def page():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    int_features = [[int(x) for x in request.form.values()]]
    final_features = fits.transform(int_features)
    prediction = model.predict(final_features)
    # output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Population should be {}'.format(int(prediction[0])))

if __name__ == "__main__" :
    app.run(port=5001,debug = True)
