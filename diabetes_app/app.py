from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)

# Load the XGBoost model
model = joblib.load('D:/VS Code/Coding/Machine Learning/GroupProject/diabetes_app/diabetes_xgb_model.joblib')

# Load the scaler object saved during training
scaler = joblib.load('D:/VS Code/Coding/Machine Learning/GroupProject/diabetes_app/standard_scaler.pkl')

# Define feature names (consistent with training)
required_columns = [
    'Age', 'Ethnicity', 'SocioeconomicStatus', 'EducationLevel', 'BMI',
    'Smoking', 'AlcoholConsumption', 'PhysicalActivity', 'DietQuality',
    'SleepQuality', 'Hypertension', 'SystolicBP', 'DiastolicBP',
    'FastingBloodSugar', 'HbA1c', 'SerumCreatinine', 'BUNLevels',
    'CholesterolTotal', 'CholesterolLDL', 'CholesterolHDL', 'Statins',
    'FrequentUrination', 'ExcessiveThirst', 'UnexplainedWeightLoss',
    'FatigueLevels', 'BlurredVision', 'QualityOfLifeScore',
    'MedicalCheckupsFrequency', 'MedicationAdherence', 'HealthLiteracy'
]

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/batch_predict', methods=['POST'])
def batch_predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    try:
        # Read the uploaded CSV file
        df = pd.read_csv(file)

        # Check if the CSV file contains all required columns
        if not all(col in df.columns for col in required_columns):
            missing_cols = [col for col in required_columns if col not in df.columns]
            return jsonify({'error': f'CSV file missing required columns: {missing_cols}'}), 400

        # Extract input features (30 columns)
        X = df[required_columns]

        # Standardize the input data (using the scaler from training)
        X_scaled = scaler.transform(X)

        # Check if the model is loaded
        if model is None:
            return jsonify({'error': 'Model not loaded. Please load a trained model first.'}), 503

        # Perform prediction
        predictions = model.predict(X_scaled)

        # Print the first few predictions (for debugging, logging)
        print("Sample predictions from batch:", predictions[:10])

        # Prepare output data, returning only the specified columns
        output_df = df[['FastingBloodSugar', 'HbA1c', 'FrequentUrination', 'Hypertension',
                        'ExcessiveThirst', 'UnexplainedWeightLoss', 'BlurredVision',
                        'SocioeconomicStatus']].copy()

        # Convert prediction results to Yes/No
        output_df['Diabetic'] = ['Yes' if pred == 1 else 'No' for pred in predictions]

        # Return the output as JSON
        return jsonify(output_df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)