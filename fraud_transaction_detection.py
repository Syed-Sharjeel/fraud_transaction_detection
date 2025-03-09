import streamlit as st
import pandas as pd
import numpy as np
import time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Loading Data & Dropping Irrelevant Features
data = pd.read_csv(r'synthetic_fraud_dataset.csv')
data = data.drop(['Transaction_ID', 'User_ID', 'Location', 'Merchant_Category', 'IP_Address_Flag','Card_Type', 'Card_Age','Is_Weekend','Timestamp'], axis=1)

# One Hot Encoding on Authentication_Method, Device_Type, Transaction_Type
data = pd.get_dummies(data, columns=['Authentication_Method', 'Device_Type', 'Transaction_Type'])

# Separate Feature and Target Variable
X = data.drop(['Fraud_Label'], axis=1)
y = data['Fraud_Label']

# Splitting Data into Training and Testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


feature_names = [ "Transaction_Amount", "Account_Balance", "Previous_Fraudulent_Activity", "Daily_Transaction_Count", "Avg_Transaction_Amount_7d", "Failed_Transaction_Count_7d",
    "Transaction_Distance", "Risk_Score", "Authentication_Method_Biometric", "Authentication_Method_OTP", "Authentication_Method_PIN", "Authentication_Method_Password",
    "Device_Type_Laptop", "Device_Type_Mobile", "Device_Type_Tablet", "Transaction_Type_ATM Withdrawal", "Transaction_Type_Bank Transfer", "Transaction_Type_Online", "Transaction_Type_POS"
]

st.write("\nWELCOME TO FRAUD TRANSACTION DETECTION SYSTEM")
# User Inputs

with st.form("user_inputs"):
    
    feature_names = [
        "Transaction_Amount", "Account_Balance", "Previous_Fraudulent_Activity","Daily_Transaction_Count", "Avg_Transaction_Amount_7d", "Failed_Transaction_Count_7d",
        "Transaction_Distance", "Risk_Score","Authentication_Method_Biometric", "Authentication_Method_OTP", "Authentication_Method_PIN", "Authentication_Method_Password",
        "Device_Type_Laptop", "Device_Type_Mobile", "Device_Type_Tablet","Transaction_Type_ATM Withdrawal", "Transaction_Type_Bank Transfer", "Transaction_Type_Online", "Transaction_Type_POS"
    ]

    # User Inputs
    transaction_amount = st.number_input("Enter Transaction Amount: ")
    account_balance = st.number_input("Enter Account Balance: ")
    previous_fraud = st.number_input("Enter Previous Fraudulent Activity (0: No, 1: Yes): ")
    daily_transaction_count = st.number_input("Enter Daily Transaction Count: ")
    avg_transaction_amount_7d = st.number_input("Enter Average Transaction Amount (last 7 days): ")
    failed_transaction_count_7d = st.number_input("Enter Failed Transaction Count (last 7 days): ")
    transaction_distance = st.number_input("Enter Transaction Distance (in km): ")
    risk_score = st.number_input("Enter Risk Score (0-1 range): ")
    
    # Encoded Inputs
    auth_method = st.radio("Enter Authentication Method (Biometric/OTP/PIN/Password): ", options=['Biometric', 'OTP', 'PIN', 'Password'])
    authentication_methods = {
        "Biometric": [1, 0, 0, 0],
        "OTP": [0, 1, 0, 0],
        "PIN": [0, 0, 1, 0],
        "Password": [0, 0, 0, 1]
    }
    authentication_method_biometric, authentication_method_otp, authentication_method_pin, authentication_method_password = authentication_methods.get(auth_method, [0, 0, 0, 0])

    device_type = st.radio("Enter Device Type (Laptop/Mobile/Tablet): ", options=['Laptop', 'Mobile', 'Tablet'])
    device_types = {
        "Laptop": [1, 0, 0],
        "Mobile": [0, 1, 0],
        "Tablet": [0, 0, 1]
        }
    device_type_laptop, device_type_mobile, device_type_tablet = device_types.get(device_type, [0, 0, 0])

    transaction_type = st.radio("Enter Transaction Type: ", options=['ATM Withdrawal', 'Bank Transfer', 'Online', 'POS'])
    transaction_types = {
        "ATM Withdrawal": [1, 0, 0, 0],
        "Bank Transfer": [0, 1, 0, 0],
        "Online": [0, 0, 1, 0],
        "POS": [0, 0, 0, 1]
    }
    transaction_type_atm, transaction_type_bank_transfer, transaction_type_online, transaction_type_pos = transaction_types.get(transaction_type, [0, 0, 0, 0])
    
    # Creating final input array
    X_new = np.array([transaction_amount, account_balance, previous_fraud, daily_transaction_count, avg_transaction_amount_7d, failed_transaction_count_7d, transaction_distance, 
            risk_score,authentication_method_biometric, authentication_method_otp, authentication_method_pin, authentication_method_password, device_type_laptop, 
            device_type_mobile, device_type_tablet, transaction_type_atm, transaction_type_bank_transfer, transaction_type_online, transaction_type_pos]).reshape(1, -1)
    
    # Converting array to DataFrame
    X_new_df = pd.DataFrame(X_new, columns=feature_names)
    
    submit = st.form_submit_button("Check for Fraud")
    print("at SUBMIT")
if submit:
    print("SUBMITTED")
    print("LOADING MODEL")
    # Loading Model
    with st.spinner("Loading ..."):
        time.sleep(1)
        model = LogisticRegression(max_iter=20000)
        model.fit(X_train, y_train)

        # Prediction
        y_pred = model.predict(X_test)
        print("MODEL LOADED")
        prediction = model.predict(X_new)
    # Final Result   
    st.write("RESULT: ")
    if prediction[0] == 1:
        st.write("\t\tFraud Detected!")
    elif prediction[0] == 0:
        st.write("\t\tTransaction is Safe.")