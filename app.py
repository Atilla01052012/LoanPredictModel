
import streamlit as st
import pickle
import pandas as pd

# Загрузка модели
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Loan Prediction App")

st.write("Введите данные клиента")

# Поля ввода
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])

applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)

loan_amount = st.number_input("Loan Amount", min_value=0.0)
loan_amount_term = st.number_input("Loan Amount Term", min_value=0.0)

credit_history = st.selectbox("Credit History", [1.0, 0.0])

property_area = st.selectbox(
    "Property Area",
    ["Urban", "Rural", "Semiurban"]
)

# Кнопка предсказания
if st.button("Predict"):

    # Преобразование данных
    gender = 1 if gender == "Male" else 0
    married = 1 if married == "Yes" else 0
    education = 1 if education == "Graduate" else 0
    self_employed = 1 if self_employed == "Yes" else 0

    dependents_map = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3+": 3
    }

    property_area_map = {
        "Urban": 1,
        "Rural": 0,
        "Semiurban": 2
    }

    dependents = dependents_map[dependents]
    property_area = property_area_map[property_area]

    # DataFrame
    data = pd.DataFrame([{
        'Gender': gender,
        'Married': married,
        'Dependents': dependents,
        'Education': education,
        'Self_Employed': self_employed,
        'ApplicantIncome': applicant_income,
        'CoapplicantIncome': coapplicant_income,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_amount_term,
        'Credit_History': credit_history,
        'Property_Area': property_area
    }])

    # Предсказание
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")

