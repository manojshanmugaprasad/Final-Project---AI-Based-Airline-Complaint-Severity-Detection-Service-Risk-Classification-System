
# AI-Based Airline Complaint Severity Detection & Service Risk Classification System

## Project Overview
This project analyzes airline customer reviews and predicts complaint severity levels (Low, Medium, High, Critical) and service risk (Risk / No Risk) using Natural Language Processing, Machine Learning, Deep Learning, and Transformer models.

The system is deployed as a Streamlit web application with interactive dashboards and prediction capabilities.


## Problem Statement
Airlines receive large volumes of customer complaints and reviews. Identifying high-severity complaints and service risks manually is difficult and time-consuming. This project builds an AI system to automatically classify complaint severity and service risk from airline review text and service ratings.

---

## Dataset Description
Dataset: Airline Reviews Dataset  
Source: airlinequality.com  

Features include:
- Airline Name
- Overall Rating
- Review Title
- Review
- Seat Comfort
- Cabin Staff Service
- Food & Beverages
- Ground Service
- Inflight Entertainment
- Wifi & Connectivity
- Value for Money
- Recommended

---

## Project Pipeline
1. Data Cleaning & Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. ML Models (Logistic Regression, Random Forest, XGBoost)
5. Deep Learning Models (LSTM, CNN)
6. Transformer Models (BERT / DistilBERT)
7. Model Evaluation & Comparison
8. Streamlit Application Development
9. Optional AWS Deployment

---

## Models Used
- Logistic Regression
- Linear SVM
- Random Forest
- XGBoost
- BiLSTM / CNN
- DistilBERT / BERT

---

## Model Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Precision-Recall Curve
- Confusion Matrix

---

## Streamlit Application
The Streamlit app contains:
- Introduction Page
- EDA Dashboard
- Severity & Risk Prediction Page
- Single Review Prediction
- Bulk CSV Prediction
- Highlighted Complaint Words

---

## How to Run the Project
pip install -r requirements.txt
streamlit run app/app.py
