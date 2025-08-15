import streamlit as st
import pandas as pd
import joblib
import base64

# ----- Add Background Image via CSS -----
def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .stButton>button {{
        background-color: #0a9396;
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Call the function with your image path
add_bg_from_local("assets/background.jpg")

# --------------------------------------------------

# Load model and features
model = joblib.load("model/salary_model.pkl")
feature_names = joblib.load("model/feature_names.pkl")

st.set_page_config(page_title="Salary Predictor", layout="centered")
st.title("💼 Salary Predictor for Data Science, AI, ML Jobs")

# User input with placeholders
job_title = st.selectbox("Job Title", ['Select a job title', 'Data Scientist', 'Machine Learning Engineer', 'AI Specialist'])
employment_type = st.selectbox("Employment Type", ['Select employment type', 'Full-time', 'Part-time', 'Contract'])
company_size = st.selectbox("Company Size", ['Select company size', 'Small', 'Medium', 'Large'])
experience_level = st.selectbox("Experience Level", ['Select experience level', 'Junior', 'Mid', 'Senior', 'Expert'])

# Validate input
if (
    job_title != 'Select a job title' and
    employment_type != 'Select employment type' and
    company_size != 'Select company size' and
    experience_level != 'Select experience level'
):
    input_dict = {
        'job_title': job_title,
        'employment_type': employment_type,
        'company_size': company_size,
        'experience_level': experience_level
    }

    input_df = pd.DataFrame([input_dict])
    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=feature_names, fill_value=0)

    if st.button("Predict Salary"):
        salary = model.predict(input_encoded)[0]
        st.success(f"💰 Predicted Salary: ${salary:,.2f}")
else:
    st.warning("⚠️ Please select all fields to make a prediction.")
