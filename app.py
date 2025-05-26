import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('random_forest_email_model.pkl')

st.set_page_config(layout="centered")


st.title("Email Marketing - Customer Visit Prediction")
st.markdown("Fill in the customer details to predict whether they will visit the online store based on being sent a marketing email.")

with st.form("prediction_form"):
    st.markdown("### Customer Information")
    col1, col2 = st.columns(2, gap="medium")

    with col1:
        purchase = st.number_input("Total Purchase Amount (£)", min_value=0.0, value=100.0)
        employed = st.selectbox("Employed?", ["Yes", "No"])
        email_segment = st.selectbox("Email Segment", ['Womens E-Mail', 'Mens E-Mail'])
        zip_area = st.selectbox("Zip Area", ['Urban', 'Surburban', 'Rural'])
        age = st.slider("Age", 18, 100, 35)
        recency = st.slider("How many days since the last purchase?", 0, 100, 10)
        
    with col2:    
        mens = st.selectbox("Bought Menswear?", ["Yes", "No"])
        womens = st.selectbox("Bought Womenswear?", ["Yes", "No"])
        new_customer = st.selectbox("New Customer?", ["Yes", "No"])
        phone = st.selectbox("Phone Number Available?", ["Yes", "No"])
        payment_card = st.selectbox("Payment Card Available?", ["Yes", "No"])
        channel = st.selectbox("Channel", ['Web', 'Phone', 'Both'])

    submitted = st.form_submit_button("Predict")

if submitted:
    input_data = pd.DataFrame([{
    'recency': recency,
    'purchase': purchase,
    'mens': 1 if mens == 'Yes' else 0,
    'womens': 1 if womens == 'Yes' else 0,
    'new_customer': 1 if new_customer == 'Yes' else 0,
    'age': age,
    'employed': 1 if employed == 'Yes' else 0,
    'phone': 1 if phone == 'Yes' else 0,
    'payment_card': 1 if payment_card == 'Yes' else 0,

    'email_segment_Mens E-Mail': 1 if email_segment == 'Mens E-Mail' else 0,
    'email_segment_Womens E-Mail': 1 if email_segment == 'Womens E-Mail' else 0,

    'channel_Multichannel': 1 if channel == 'Both' else 0,
    'channel_Phone': 1 if channel == 'Phone' else 0,
    'channel_Web': 1 if channel == 'Web' else 0,

    'zip_area_Rural': 1 if zip_area == 'Rural' else 0,
    'zip_area_Suburban': 1 if zip_area == 'Suburban' else 0,
    'zip_area_Urban': 1 if zip_area == 'Urban' else 0,
}])
    st.markdown("### Input Data")
    st.write(input_data)

    st.markdown("### Prediction")
    
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.success(f"✅ Likely to visit the store. (Probability: {prob:.2%})")
    else:
        st.warning(f"❌ Unlikely to visit the store. (Probability: {prob:.2%})")
