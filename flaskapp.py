import pickle
import pandas as pd
import numpy as np
import pickle
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the trained student performance model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    hrs_Studied = float(request.form["hrs_Studied"])
    prev_score = float(request.form["prev_score"])
    sleep = float(request.form["sleep"])
    sample_practiced = float(request.form["sample_practiced"])
    extra_Curr = 1 if request.form["extra_Curr"].lower() == "yes" else 0

    # Prepare features for prediction (must match the exact columns the model was trained on)
    feature_names = ["hrs_studied", "prev_score", "sleep", "sample_practiced", "extra_Curr"]
    features = pd.DataFrame([[hrs_Studied, prev_score, sleep, sample_practiced, extra_Curr]], columns=feature_names)

    # Predict student performance
    prediction = model.predict(features)

    # Format the prediction output
    formatted_prediction = f"The predicted student performance score is: {round(float(prediction), 2)}"

    return render_template("result.html", prediction=formatted_prediction)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
