import streamlit as st
import pandas as pd
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

st.title("AI Airline Complaint Severity Detection & Service Risk Classification")

st.header("Project Overview")
st.write("""
This project analyzes airline customer complaints and predicts complaint severity 
and service risk level using machine learning and NLP techniques.
The system helps airlines identify high-risk complaints and improve service quality.
""")

st.header("Dataset Summary")

df = pd.read_csv("D:/AI-Based Airline Complaint Severity Detection & Service Risk Classification System/venv/Scripts/data/raw/Airline_review.csv")

st.write("Dataset Shape:", df.shape)
st.write("Columns:", df.columns.tolist())

st.write("Sample Data")
st.dataframe(df.head())

st.header("Business Use Cases")
st.write("""
• Identify high severity complaints automatically  
• Predict service risk level  
• Improve customer service quality  
• Prioritize critical complaints  
• Monitor airline performance  
""")