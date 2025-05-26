# 📬 Email Marketing Visit Prediction

This project uses machine learning to predict whether a customer will visit an online store after receiving an email campaign. It includes a deployed Streamlit app for real-time predictions and a Tableau dashboard for exploratory data analysis.

## 🔍 Project Overview
- **Objective**: Predict customer visits based on demographic and behavioural data
- **Model**: Random Forest classifier
- **Deployment**: Streamlit web app + Tableau dashboard

## 🚀 Features
- Streamlit app with user input + random data generation
- Classification report, ROC-AUC evaluation, and feature importance analysis
- Tableau dashboard with visual insights (age, channel, email type, spend)

## 📁 Files
- `app.py` – Streamlit app for real-time prediction
- `random_forest_email_model.pkl` – Trained Random Forest model
- `email_marketing.ipynb` – Data cleaning, EDA, and model training notebook

## 📊 Demo
Live Streamlit App → [Streamlit App](https://email-marketing-random-forest.streamlit.app/)  
Tableau Dashboard → [Email Marketing - Exploratory Data Analysis](https://public.tableau.com/views/EmailMarketing-ExploratoryAnalysis/EmailMarketing-EDADashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## 🔧 Tech Stack
- Python (pandas, scikit-learn, imblearn, Streamlit)
- Tableau (EDA dashboard)
- Jupyter Notebook (model development)

## 🧠 Highlights
- Applied oversampling to handle class imbalance
- Evaluated multiple models; Random Forest selected for best performance
- Deployed an intuitive web interface for end-users

## 📦 Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run Streamlit app: `streamlit run app.py`
