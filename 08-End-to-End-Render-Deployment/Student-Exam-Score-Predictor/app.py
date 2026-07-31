from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("models/model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    hours = float(request.form["Hours_Studied"])
    attendance = float(request.form["Attendance"])
    parental = request.form["Parental_Involvement"]
    resources = request.form["Access_to_Resources"]
    activities = request.form["Extracurricular_Activities"]
    sleep = float(request.form["Sleep_Hours"])
    previous = float(request.form["Previous_Scores"])

    input_df = pd.DataFrame({
        "Hours_Studied": [hours],
        "Attendance": [attendance],
        "Parental_Involvement": [parental],
        "Access_to_Resources": [resources],
        "Extracurricular_Activities": [activities],
        "Sleep_Hours": [sleep],
        "Previous_Scores": [previous]
    })

    prediction = model.predict(input_df)[0]

    return render_template(
        "index.html",
        prediction_text=f"Predicted Exam Score: {prediction:.2f}"
    )


if __name__ == "__main__":
    app.run(debug=True)