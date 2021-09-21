from flask import Flask, jsonify, request, render_template 
# import json
import pickle
import pandas as pd

print(">>>>> LOADING MODELS")
loaded_scaler = pickle.load(open("./models/ch10_scaler.pickle", 'rb'))
loaded_clf = pickle.load(open("./models/ch10_rfc_clf.pickle", 'rb'))
print(">>>>> MODELS LOADED")

def predict_diagnosis(inputData, scaler, model):
    """
    Function that takes a list of measurements, scales them, and returns a prediction
    """
    inputDataDF = pd.DataFrame([inputData])
    scaledInputData = scaler.transform(inputDataDF)
    prediction = model.predict(scaledInputData)
    return prediction[0]


# EB looks for an 'application' callable by default.
application = Flask(__name__)
application.config['EXPLAIN_TEMPLATE_LOADING'] = True

# add a rule for the index page.

@application.route('/')
def home():
    return render_template('./templates/index.html')

@application.route('/hello')
def hello():
    return "Hello Biotech World!"

@application.route('/prediction', methods = ["POST"])
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
    
    return render_template('./templates/index.html', prediction_text = '" {} "'.format(prediction))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()