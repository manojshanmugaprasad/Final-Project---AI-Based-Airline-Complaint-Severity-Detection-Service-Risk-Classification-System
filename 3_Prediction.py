import streamlit as st
import sys
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

# Get project root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

import streamlit as st
from Scripts.src.utils import predict
import pandas as pd

st.title("Severity & Risk Prediction")

# -----------------------------
# Single Prediction
# -----------------------------
st.subheader("Single Review Prediction")

review_text = st.text_area("Enter Review Text")

overall_rating = st.slider("Overall Rating", 1, 10, 5)
seat_comfort = st.slider("Seat Comfort", 1, 5, 3)
cabin_staff = st.slider("Cabin Staff Service", 1, 5, 3)
food = st.slider("Food & Beverages", 1, 5, 3)
ground = st.slider("Ground Service", 1, 5, 3)
entertainment = st.slider("Inflight Entertainment", 1, 5, 3)
wifi = st.slider("Wifi & Connectivity", 1, 5, 3)
value = st.slider("Value For Money", 1, 5, 3)

if st.button("Predict"):

    ratings = {
        "Overall_Rating": overall_rating,
        "Seat Comfort": seat_comfort,
        "Cabin Staff Service": cabin_staff,
        "Food & Beverages": food,
        "Ground Service": ground,
        "Inflight Entertainment": entertainment,
        "Wifi & Connectivity": wifi,
        "Value For Money": value
    }

    severity, risk, prob = predict(review_text, ratings)

    st.success(f"Severity Prediction: {severity}")
    st.warning(f"Risk Prediction: {risk}")
    st.info(f"Risk Probability: {prob:.2f}")

# -----------------------------
# Bulk Prediction
# -----------------------------
st.subheader("Bulk Prediction")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.write("Columns in CSV:", df.columns)

    text_column = st.selectbox("Select Review Text Column", df.columns)

    # Fill missing values
    df = df.fillna({
        "Overall_Rating": 5,
        "Seat Comfort": 3,
        "Cabin Staff Service": 3,
        "Food & Beverages": 3,
        "Ground Service": 3,
        "Inflight Entertainment": 3,
        "Wifi & Connectivity": 3,
        "Value For Money": 3
    })

    results = []

    for i, row in df.iterrows():
        text = str(row[text_column])

        ratings = {
            "Overall_Rating": row["Overall_Rating"],
            "Seat Comfort": row["Seat Comfort"],
            "Cabin Staff Service": row["Cabin Staff Service"],
            "Food & Beverages": row["Food & Beverages"],
            "Ground Service": row["Ground Service"],
            "Inflight Entertainment": row["Inflight Entertainment"],
            "Wifi & Connectivity": row["Wifi & Connectivity"],
            "Value For Money": row["Value For Money"]
        }

        severity, risk, prob = predict(text, ratings)

        results.append([severity, risk, prob])

    df["Predicted_Severity"] = [r[0] for r in results]
    df["Risk_Flag"] = [r[1] for r in results]
    df["Risk_Probability"] = [r[2] for r in results]

    st.dataframe(df)

    

    st.download_button(
        "Download Results",
        df.to_csv(index=False),
        "predictions.csv"
    )


st.subheader("Highlighted Complaint Words")

important_words = [
    "delay","delayed","late","cancelled","canceled","refund","rude",
    "baggage","lost","luggage","dirty","bad","worst","poor","terrible",
    "seat","food","wifi","service","staff","boarding","problem","issue",
    "complaint","uncomfortable","broken","smell","noise","crowded"
]

def highlight_text(text, keywords):
    words = text.split()
    highlighted_text = ""

    for word in words:
        if word.lower() in keywords:
            highlighted_text += f"<span style='color:red; font-weight:bold'>{word}</span> "
        else:
            highlighted_text += word + " "

    return highlighted_text

if review_text:
    highlighted_review = highlight_text(review_text, important_words)
    st.markdown(highlighted_review, unsafe_allow_html=True)