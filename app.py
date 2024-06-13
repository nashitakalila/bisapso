from flask import Flask, request, jsonify
from joblib import load
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
model = load('stroke.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    # Ensure the order of features matches the order expected by the model
    feature_values = [
        data['age'], 
        data['avg_glucose_level'], 
        data['bmi'], 
        data['gender'], 
        data['ever_married'], 
        data['work_type'], 
        data['Residence_type'], 
        data['smoking_status']
    ]
    
    # Since the model expects a DataFrame, we convert our list to a DataFrame
    features_df = pd.DataFrame([feature_values], columns=['age', 'avg_glucose_level', 'bmi', 'gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status'])
    
    # Predict using the model
    prediction = model.predict(features_df)
    output = prediction[0]
    return jsonify({'stroke_prediction': int(output)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
