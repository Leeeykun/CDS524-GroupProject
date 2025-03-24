# Diabetes Prediction System

![Python](https://img.shields.io/badge/Python-3.12-blue) ![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.2-orange) ![Flask](https://img.shields.io/badge/Flask-2.3.3-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

## Project Overview

The Diabetes Prediction System is a machine learning-based tool designed to predict the likelihood of diabetes in patients using their health data. The system employs various feature selection methods and machine learning models for data analysis, and provides batch prediction functionality through a **Flask**-based web service. The front end interacts with the back end via an HTML page, allowing users to upload a CSV file to obtain prediction results.

This project includes the following main features:
- Data cleaning and preprocessing
- Multiple feature selection methods (F-test, Mutual Information, RFE, Random Forest Feature Importance, L1 Regularization)
- Training and evaluation of various machine learning models (Logistic Regression, Random Forest, XGBoost, MLP, Ensemble Model)
- Flask web service supporting batch predictions and returning results in JSON format

## Dataset

The project uses the dataset `p1_before_scaling.csv`, which contains 1879 records and 46 features, including:
- Basic patient information (e.g., age, gender, BMI)
- Lifestyle factors (e.g., smoking, alcohol consumption, physical activity)
- Clinical indicators (e.g., blood pressure, blood sugar, HbA1c)
- Target variable `Diagnosis` (0 for non-diabetic, 1 for diabetic)
- For a detailed description of the variables, please refer to `Description of the variable.pdf`.

## Features

1. **Data Cleaning**:
   - Check for missing values and duplicates

2. **Feature Selection**:
   - Use multiple methods to select important features:
     - F-test (`SelectKBest` with `f_classif`)
     - Mutual Information (`SelectKBest` with `mutual_info_classif`)
     - Recursive Feature Elimination (RFE with RandomForestClassifier)
     - Random Forest Feature Importance
     - L1 Regularization (Lasso)

3. **Model Training and Evaluation**:
   - Baseline model: Logistic Regression
   - Other models: Random Forest, XGBoost, MLP, Ensemble Model (Stacking)
   - Evaluation metrics: Cross-validation accuracy, confusion matrix, classification report, ROC curve, and AUC score

4. **Flask Web Service**:
   - Built with Flask to support batch predictions
   - Users can upload a CSV file through the front-end page to obtain diabetes prediction results
   - Returns prediction results in JSON format, including selected original features and the prediction result (`Diabetic` column, with values "Yes" or "No")

## Installation

### Environment Requirements
- Python 3.12 or higher
- It is recommended to use a virtual environment (e.g., `venv` or `conda`)

### Installation Steps
1. **Clone the Project Repository**:
   ```bash
   git clone https://github.com/Leeeykun/CDS524-GroupProject.git
   cd CDS524-GroupProject

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Start the Flask Application**:
  Run the following command in the project root directory to start the Flask application:
   ```bash
   python app.py
 The Flask application will start, and the default address is http://127.0.0.1:5000.

4.**Use the Web Interface**:
 Open your browser and visit http://127.0.0.1:5000.
 Upload a CSV file on the page (ensure it contains all required feature columns).
 After submission, the page will display the prediction results (returned in JSON format).
