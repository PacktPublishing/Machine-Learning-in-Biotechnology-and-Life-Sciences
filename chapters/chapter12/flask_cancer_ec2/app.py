from flask import Flask, jsonify, request, render_template 
import json
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

loaded_scaler = pickle.load(open("./models/ch11_scaler.pickle", 'rb'))
loaded_clf = pickle.load(open("./models/ch11_rfc_clf.pickle", 'rb'))

def predict_diagnosis(inputData, scaler, model):
    """
    Function that takes a list of measurements, scales them, and returns a prediction
    """
    inputDataDF = pd.DataFrame([inputData])
    scaledInputData = scaler.transform(inputDataDF)
    prediction = model.predict(scaledInputData)
    return prediction[0]


app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test')
def hello():
    return "hello biotech world!"

@app.route('/prediction', methods = ["POST"])
def prediction():
    print(request.form.values())
    radius_mean = request.form.get("radius_mean")
    texture_mean = request.form.get("texture_mean")
    smoothness_mean = request.form.get("smoothness_mean")
    texture_se = request.form.get("texture_se")
    smoothness_se = request.form.get("smoothness_se")
    symmetry_se = request.form.get("symmetry_se")
    input_features = [radius_mean, texture_mean, smoothness_mean, texture_se, smoothness_se, symmetry_se]
    prediction = predict_diagnosis(input_features, loaded_scaler, loaded_clf)
    prediction = "Malignant" if prediction == "M" else "Benign"
    
    return render_template('index.html', prediction_text = '" {} "'.format(prediction))

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=False, host='0.0.0.0', port=5000)