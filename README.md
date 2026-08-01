# 🚀 AI & Machine Learning Projects

A collection of **9 hands-on Artificial Intelligence and Machine Learning projects** developed as part of my AI/ML learning and internship work.

This repository demonstrates practical implementation across **Machine Learning, Deep Learning, Computer Vision, Reinforcement Learning, Recommendation Systems, ML Deployment, and Retrieval-Augmented Generation (RAG).**

---

## 📂 Projects

| # | Project | Domain | Key Concepts |
|---|---|---|---|
| 01 | Adult Census Income Classification | Machine Learning | Classification, Data Preprocessing, Model Evaluation |
| 02 | CIFAR-10 Image Classification using CNN | Deep Learning | CNN, Image Classification, TensorFlow/Keras |
| 03 | LFW Face Recognition | Computer Vision | Face Recognition, PCA, SVM |
| 04 | Cancer Detection using MRI | Deep Learning / Healthcare AI | Medical Image Classification, CNN |
| 05 | CartPole Reinforcement Learning | Reinforcement Learning | Q-Learning, Agent-Environment Interaction |
| 06 | LunarLander Reinforcement Learning | Reinforcement Learning | DQN, Gymnasium, Stable-Baselines3 |
| 07 | Movie Recommendation System | Recommendation Systems | NLP, Content-Based Filtering, Cosine Similarity |
| 08 | Student Exam Score Predictor | ML Deployment | Regression, Flask, Render |
| 09 | RAG Chatbot | Generative AI | RAG, Gemini, FAISS, Embeddings |

---

# 🧠 Project Overview

## 01 — Adult Census Income Classification

A machine learning classification project that predicts whether an individual's annual income exceeds a specified threshold based on demographic and employment-related attributes from the Adult Census dataset.

The project covers the complete traditional ML workflow, including data preprocessing, feature handling, model training, prediction, and evaluation.

**Key Concepts**
- Supervised Machine Learning
- Binary Classification
- Data Preprocessing
- Feature Engineering
- Model Evaluation

**Technologies:** Python, Pandas, NumPy, Scikit-learn

---

## 02 — CIFAR-10 Image Classification using CNN

A deep learning image classification project using the **CIFAR-10 dataset**.

A Convolutional Neural Network (CNN) is trained to classify images into different object categories by automatically learning spatial and visual features from image data.

**Key Concepts**
- Deep Learning
- Convolutional Neural Networks
- Image Classification
- Model Training & Evaluation

**Technologies:** Python, TensorFlow/Keras, NumPy, Matplotlib

---

## 03 — LFW Face Recognition

A machine learning-based face recognition system developed using the **Labeled Faces in the Wild (LFW)** dataset.

The project demonstrates dimensionality reduction and classification techniques for recognizing individuals from facial images.

**Key Concepts**
- Computer Vision
- Face Recognition
- Principal Component Analysis (PCA)
- Support Vector Machines
- Dimensionality Reduction

**Technologies:** Python, Scikit-learn, NumPy, Matplotlib

---

## 04 — Cancer Detection using MRI

A medical imaging project designed to classify MRI images using deep learning techniques.

The project demonstrates how computer vision and neural networks can be applied to healthcare-related image classification problems.

**Key Concepts**
- Medical Image Analysis
- Deep Learning
- Convolutional Neural Networks
- Image Preprocessing
- Classification

**Technologies:** Python, TensorFlow/Keras, NumPy, Matplotlib

---

## 05 — CartPole Reinforcement Learning

A reinforcement learning project in which an AI agent learns to balance a pole mounted on a moving cart.

The agent interacts with the CartPole environment, observes its current state, performs actions, receives rewards, and gradually improves its decision-making strategy.

**Key Concepts**
- Reinforcement Learning
- Agent-Environment Interaction
- State & Action Spaces
- Reward Optimization
- Q-Learning

**Technologies:** Python, Gymnasium, NumPy

---

## 06 — LunarLander Reinforcement Learning using DQN

A reinforcement learning agent trained to successfully control and land a spacecraft in the **LunarLander environment**.

A **Deep Q-Network (DQN)** is used to learn an optimal action policy from interactions and rewards received from the environment.

**Key Concepts**
- Deep Reinforcement Learning
- Deep Q-Networks
- Experience Replay
- Reward-Based Learning
- Policy Learning

**Technologies:** Python, Gymnasium, Stable-Baselines3, PyTorch, Box2D

---

## 07 — Movie Recommendation System

A **content-based movie recommendation system** developed using movie metadata.

Information including movie genres, keywords, cast, crew, and overview is transformed into feature representations. Cosine similarity is then used to identify movies with similar content.

**Key Concepts**
- Recommendation Systems
- Content-Based Filtering
- Natural Language Processing
- Feature Extraction
- Cosine Similarity

**Technologies:** Python, Pandas, NumPy, Scikit-learn, NLP

---

## 08 — Student Exam Score Predictor

An **end-to-end machine learning web application** that predicts a student's exam score using academic and lifestyle-related input features.

The project demonstrates the complete ML lifecycle from model training and serialization to integration with a Flask web application and cloud deployment using **Render**.

**Key Concepts**
- Regression
- Feature Preprocessing
- Model Training
- Model Serialization
- Flask Integration
- Cloud Deployment

**Technologies:** Python, Pandas, Scikit-learn, Flask, HTML, CSS, Gunicorn, Render

---

## 09 — RAG Chatbot

A **Retrieval-Augmented Generation (RAG) chatbot** that allows users to interact with PDF documents using natural-language questions.

The application extracts document text, divides it into manageable chunks, generates vector embeddings, stores them in a **FAISS vector database**, retrieves relevant context for a user's question, and provides that context to **Google Gemini** for answer generation.

### RAG Pipeline

```text
PDF Document
     │
     ▼
Text Extraction
     │
     ▼
Text Chunking
     │
     ▼
Vector Embeddings
     │
     ▼
FAISS Vector Store
     │
     ▼
Semantic Search
     │
     ▼
Relevant Context
     │
     ▼
Question + Context
     │
     ▼
Google Gemini
     │
     ▼
Grounded Answer
```

**Key Concepts**
- Generative AI
- Retrieval-Augmented Generation
- Large Language Models
- Vector Embeddings
- Vector Databases
- Semantic Search
- Prompt Grounding

**Technologies:** Python, Flask, Google Gemini API, FAISS, PyPDF, NumPy

---

# 🛠️ Technical Skills Demonstrated

### Machine Learning
- Classification
- Regression
- Data Preprocessing
- Feature Engineering
- Model Training
- Model Evaluation
- Scikit-learn

### Deep Learning & Computer Vision
- Neural Networks
- Convolutional Neural Networks
- Image Classification
- Face Recognition
- Medical Image Analysis
- TensorFlow / Keras
- PyTorch

### Reinforcement Learning
- Q-Learning
- Deep Q-Networks (DQN)
- Gymnasium
- Stable-Baselines3
- Reward-Based Learning
- Agent-Environment Interaction

### NLP & Recommendation Systems
- Text Processing
- Feature Extraction
- Content-Based Filtering
- Cosine Similarity
- Semantic Search

### Generative AI
- Large Language Models
- Retrieval-Augmented Generation (RAG)
- Google Gemini
- Vector Embeddings
- FAISS Vector Database
- Context Retrieval

### Deployment & Development
- Flask
- HTML/CSS
- Gunicorn
- Render
- Git
- GitHub
- Python Virtual Environments

---

# 📁 Repository Structure

```text
AI-ML-Projects/
│
├── 01-Adult-Census-Income-Classification/
│
├── 02-CIFAR10-Image-Classification-CNN/
│
├── 03-LFW-Face-Recognition/
│
├── 04-Cancer-Detection-MRI/
│
├── 05-CartPole-RL/
│
├── 06-LunarLander-RL/
│
├── 07-Movie-Recommendation-System/
│
├── 08-End-to-End-Render-Deployment/
│   └── Student-Exam-Score-Predictor/
│
├── 09-RAG-Chatbot/
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🎯 Learning Outcomes

Through these projects, I gained practical experience in:

- Building complete machine learning pipelines
- Preprocessing and analyzing real-world datasets
- Training and evaluating classification and regression models
- Designing Convolutional Neural Networks
- Working with computer vision and medical imaging
- Implementing face recognition systems
- Training reinforcement learning agents
- Implementing Deep Q-Networks
- Building content-based recommendation systems
- Integrating ML models with Flask applications
- Deploying machine learning applications using Render
- Working with Large Language Models
- Creating Retrieval-Augmented Generation pipelines
- Generating and searching vector embeddings
- Building FAISS-based semantic retrieval systems
- Managing AI/ML projects using Git and GitHub

---

# 🚀 Future Scope

Future additions to this repository may include:

- Transformer-based NLP applications
- Advanced Computer Vision models
- AI Agents
- Multimodal AI systems
- MLOps pipelines
- Cloud-based ML APIs
- Advanced RAG architectures
- Production-ready AI applications

---

# 👩‍💻 Author

**Khushie Brahma**

Interested in **Artificial Intelligence, Machine Learning, Data Science, Generative AI, and Software Development**.

---

⭐ This repository documents my practical journey of learning and implementing AI/ML concepts through end-to-end projects.