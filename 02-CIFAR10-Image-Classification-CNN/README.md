# CIFAR-10 Image Classification using CNN

## 📌 Project Overview

This project implements a **Convolutional Neural Network (CNN)** using **TensorFlow** and **Keras** to classify images from the **CIFAR-10 dataset** into ten different object categories.

The complete deep learning workflow includes data preprocessing, visualization, CNN model development, training, evaluation, prediction, and model saving.

---

## 📂 Project Structure

```
02-CIFAR10-Image-Classification-CNN
│
├── dataset/
├── models/
│   └── cifar10_cnn_model.keras
├── notebook/
│   └── CIFAR10_Image_Classification.ipynb
├── screenshots/
├── README.md
└── requirements.txt
```

---

## 📊 Dataset

**Dataset:** CIFAR-10

- 60,000 RGB Images
- 10 Image Classes
- 32 × 32 pixels

Training Images:

- 50,000

Testing Images:

- 10,000

Classes:

- Airplane
- Automobile
- Bird
- Cat
- Deer
- Dog
- Frog
- Horse
- Ship
- Truck

---

## 🛠 Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib

---

## 🧠 CNN Architecture

- Conv2D (32 Filters)
- MaxPooling2D
- Conv2D (64 Filters)
- MaxPooling2D
- Flatten
- Dense (128)
- Dropout (0.5)
- Dense (10 Softmax)

---

## 📈 Model Performance

The model was trained for **10 epochs** using the Adam optimizer and Categorical Crossentropy loss.

Evaluation metrics include:

- Test Accuracy
- Test Loss

---

## 📸 Project Screenshots

- Dataset Information
- Sample Images
- Model Summary
- Training Output
- Accuracy Graph
- Loss Graph
- Prediction Result

---

## 💾 Saved Model

The trained CNN model is saved as:

```
models/cifar10_cnn_model.keras
```

---

## ✅ Conclusion

This project demonstrates image classification using a Convolutional Neural Network. It covers the complete deep learning pipeline from dataset loading to prediction and model persistence.