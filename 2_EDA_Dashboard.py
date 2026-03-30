import streamlit as st
import pandas as pd
import os
import base64

def add_banner():
    with open("D:/AI-Based Airline Complaint Severity Detection & Service Risk Classification System/sustainability-report-landing-page-banner_final.png", "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <div style="width:100%; margin-bottom:20px;">
            <img src="data:image/png;base64,{encoded}" 
            style="width:100%; border-radius:10px;">
        </div>
        """,
        unsafe_allow_html=True
    )

add_banner()

st.title("EDA Dashboard")

# Paths
comparison_path = "D:/AI-Based Airline Complaint Severity Detection & Service Risk Classification System/venv/Scripts/models/model_comparison.csv"

severity_img = "D:/AI-Based Airline Complaint Severity Detection & Service Risk Classification System/Severity_Distribution.png"
risk_img = "D:/AI-Based Airline Complaint Severity Detection & Service Risk Classification System/Risk_Flag.png"
airline_img = "D:/AI-Based Airline Complaint Severity Detection & Service Risk Classification System/Top10_Airline_vs_severity.png"
critical_wc = "D:/AI-Based Airline Complaint Severity Detection & Service Risk Classification System/Critical_Complaint_Word_Cloud.png"
low_wc = "D:/AI-Based Airline Complaint Severity Detection & Service Risk Classification System/Low_Severity_Word_Cloud.png"

cm_path = "D:/AI-Based Airline Complaint Severity Detection & Service Risk Classification System/venv/notebooks/severity_confusion_matrix.png"
roc_path = "D:/AI-Based Airline Complaint Severity Detection & Service Risk Classification System/venv/notebooks/risk_roc_curve.png"


# Severity Distribution
st.subheader("Severity Distribution")
if os.path.exists(severity_img):
    st.image(severity_img)

# Risk Distribution
st.subheader("Risk Distribution")
if os.path.exists(risk_img):
    st.image(risk_img)


# Word Clouds
st.subheader("Critical Complaint Word Cloud")
if os.path.exists(critical_wc):
    st.image(critical_wc)

st.subheader("Low Severity Word Cloud")
if os.path.exists(low_wc):
    st.image(low_wc)

# Airline vs Severity
st.subheader("Top Airlines vs Severity")
if os.path.exists(airline_img):
    st.image(airline_img)

# Model Comparison
st.subheader("Model Comparison Table")
comparison_df = pd.read_csv(comparison_path)
st.dataframe(comparison_df)

# Confusion Matrix
st.subheader("Confusion Matrix")
if os.path.exists(cm_path):
    st.image(cm_path)
else:
    st.warning("Confusion matrix image not found")

# ROC Curve
st.subheader("ROC Curve")
if os.path.exists(roc_path):
    st.image(roc_path)
else:
    st.warning("ROC curve image not found")


pr_path = "D:/AI-Based Airline Complaint Severity Detection & Service Risk Classification System/venv/notebooks/pr_curve.png"

st.subheader("Precision-Recall Curve")
if os.path.exists(pr_path):
    st.image(pr_path)
else:
    st.warning("Precision-Recall curve image not found")