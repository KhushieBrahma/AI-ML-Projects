# Brain Cancer Detection using MRI Images

## 📌 Project Overview

This project develops a **Convolutional Neural Network (CNN)** to detect the presence of brain tumors from MRI images. The model is trained using TensorFlow and Keras on a labeled MRI dataset containing **Tumor** and **No Tumor** images.

The project demonstrates a complete deep learning workflow, including image preprocessing, model training, evaluation, prediction, and model persistence.

---

## 📂 Project Structure

```
04-Cancer-Detection-MRI
│
├── dataset/
│   └── brain_tumor_dataset/
│       ├── yes/
│       └── no/
│
├── models/
│   └── brain_cancer_detection.keras
│
├── notebook/
│   └── Brain_Cancer_Detection.ipynb
│
├── screenshots/
│
├── README.md
└── requirements.txt
```

---

## 📊 Dataset

**Dataset:** Brain MRI Images for Brain Tumor Detection

Classes:

- Tumor (yes)
- No Tumor (no)

The dataset consists of MRI brain scans categorized into two classes for binary image classification.

---

## 🛠 Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib

---

## 🧠 CNN Architecture

The model consists of:

- Conv2D (32 Filters)
- MaxPooling2D
- Conv2D (64 Filters)
- MaxPooling2D
- Flatten
- Dense (128)
- Dropout (0.5)
- Dense (1, Sigmoid)

---

## 🔄 Project Workflow

1. Import Libraries
2. Load MRI Dataset
3. Data Preprocessing
4. Visualize Sample Images
5. Build CNN Model
6. Train Model
7. Evaluate Performance
8. Plot Accuracy & Loss Curves
9. Save Trained Model
10. Predict MRI Images

---

## 📈 Model Evaluation

The trained model is evaluated using:

- Validation Accuracy
- Validation Loss
- Accuracy Curve
- Loss Curve

---

## 💾 Saved Model

The trained CNN model is saved as:

```
models/brain_cancer_detection.keras
```

---

## 📸 Project Screenshots

- TensorFlow Version
- Dataset Information
- Sample MRI Images
- Model Summary
- Training Output
- Validation Accuracy
- Accuracy Graph
- Loss Graph
- Prediction Results

---

## 🚀 Future Improvements

- Increase dataset size for better generalization.
- Apply data augmentation techniques.
- Use transfer learning models such as ResNet50 or EfficientNet.
- Deploy the trained model as a web application using Streamlit or Flask.

---

## ✅ Conclusion

This project demonstrates how Convolutional Neural Networks (CNNs) can be applied to medical image classification for brain tumor detection. It covers the complete deep learning pipeline from dataset preparation to prediction and model saving.