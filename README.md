# Loan Prediction App

This project is a Machine Learning web application built with Python and Streamlit.

The model predicts whether a loan will be approved or rejected using a Decision Tree Classifier.

## Features

* Data preprocessing
* Missing value handling
* Categorical data encoding
* Decision Tree model training
* Streamlit web interface
* Model saving using pickle

---

# Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit

---

# Installation

Install required libraries:

```bash
pip install pandas scikit-learn streamlit
```

---

# Train the Model

Run the training script:

```bash
python train.py
```

This will generate:

```text
model.pkl
```

---

# Run the Streamlit App

Start the app using:

```bash
streamlit run app.py
```

---

# Project Structure

```text
project/
│
├── app.py
├── train.py
├── loan.csv
└──  model.pkl
```

---

# Dataset

Dataset file:

```text
loan.csv
```

Columns include:

* Gender
* Married
* Dependents
* Education
* Self_Employed
* ApplicantIncome
* CoapplicantIncome
* LoanAmount
* Loan_Amount_Term
* Credit_History
* Property_Area
* Loan_Status

---

# Machine Learning Model

Model used:

```text
DecisionTreeClassifier
```

Parameters:

```python
criterion='entropy'
max_depth=5
min_samples_split=10
```

---

# Author

Atilla Abbaszade
