# Fraud Detection Using Machine Learning
## Introduction
Fraudulent transactions are a major concern in financial institutions, leading to substantial losses. This project aims to detect fraud using a machine learning approach, leveraging transaction data to identify suspicious activities. The goal is to build an accurate and efficient model to classify transactions as either fraudulent or safe.
## Dataset Overview
The dataset used for this project consists of 50,000 transactions, each labeled as either fraudulent (1) or safe (0). The key features include:
- **Transaction Amount:** The value of the transaction
- **Account Balance:** The remaining balance in the account
- **Location:** The geographical origin of the transaction
- **Previous Fraudulent Activity:** Whether the user has a history of fraud
- **Daily Transaction Count:** Number of transactions done in a day
- **Authentication Method:** Whether biometric, OTP, PIN, or password was used
- **Device Type:** Whether the transaction was made from a mobile, laptop, or tablet
- **Transaction Type:** ATM withdrawal, online payment, bank transfer, etc.
## Data Preprocessing
Data preprocessing is crucial for ensuring model accuracy and efficiency. The following steps were performed:
- **Handling Missing Values:** Checking for missing values and found no missing values in dataset.
- **Handling Duplicated Values:** Checking for duplicated values and found no duplicated values in dataset.
- **Feature Encoding:** Categorical variables were transformed using one-hot encoding, while Ordinal variables were encoded by means of label encoding.
- **Feature Scaling:** Irrelevant features were dropped to improve model performance.
## Model Selection
*Logistic Regression* model was used. Logistic Regression is a supervised learning algorithm used for binary classification problems. Since fraud detection involves classifying transactions as fraudulent (1) or safe (0), Logistic Regression is a suitable choice due to:
- **Its interpretability:** Easy to understand and implement.
- **Efficiency in handling large datasets:** Performs well in high-dimensional data.
- **Robustness to multicollinearity:** Works well with correlated features.
## Model Training
The model was trained using the Scikit-learn library with the following parameters:
- *Train-Test Split:* The dataset was split into 80% training and 20% testing sets.
- *Max Iterations:* 20,000
## Model Evaluation
- *Accuracy:* Measures overall correctness of predictions.
- *Precision:* Evaluates how many of the predicted fraud cases were actually fraud.
- *Mean Squared Error:* Measures prediction error with an obtained value of 0.201.
## Result
- The model successfully classified most fraudulent and safe transactions.
- Precision and recall were balanced, indicating minimal bias.
- The feature Risk Score and Previous Fraudulent Activity had the most impact on fraud detection.
**Visualization Results:**
- Most of Fraudulent Transactions processed from Tokyo.
- Majority of Fraudulent Transactions are processed by ATM Withdrawal type.
- Majority of Fraudulent transactions done after authentication from biometric system.
## References
- Fraud Detection Transactions Dataset (By Samay Ashar, Kaggle)
- Research papers on fraud detection using machine learning
## Libraries Used:
- Numpy (Numerical Computing)
- Pandas (Data Manipulation)
- Scikit Learn (Machine Learning)
- Matplotlib (Data Visualization)
