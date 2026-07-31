# 🎓 Student Exam Score Predictor

## Overview

This is an End-to-End Machine Learning project that predicts a student's exam score based on study habits and academic factors.

The application is built using Flask and deployed on Render.

---

## Features

- Predict student exam scores
- Machine Learning model using Random Forest Regressor
- Simple and responsive web interface
- Deployable on Render

---

## Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib
- HTML/CSS
- Render

---

## Dataset

Student Performance Factors Dataset

Target Variable:
- Exam Score

Input Features:
- Hours Studied
- Attendance
- Parental Involvement
- Access to Resources
- Extracurricular Activities
- Sleep Hours
- Previous Scores

---

## Project Structure

```
Student-Exam-Score-Predictor/
│
├── data/
│   └── StudentPerformanceFactors.csv
│
├── models/
│   └── model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│
├── app.py
├── train.py
├── render.yaml
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How to Run

```bash
pip install -r requirements.txt

python train.py

python app.py
```

Open:

http://127.0.0.1:5000

---

## Future Improvements

- Better UI
- More ML models
- Hyperparameter tuning
- Feature importance visualization
- Docker deployment

---

## Author

Khushie Brahma
