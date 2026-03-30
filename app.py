import streamlit as st
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

st.set_page_config(
    page_title="Airline Complaint Severity & Risk System",
    layout="wide"
)

st.title("AI-Based Airline Complaint Severity Detection & Service Risk Classification")

st.markdown("""
Use the sidebar to navigate:
- Introduction        
- EDA Dashboard            
- Severity & Risk Prediction
""")
