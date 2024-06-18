from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the dataset
data = pd.read_csv('healthcare-dataset-stroke-data.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['age'])
    avg_glucose_level = float(request.form['avg_glucose_level'])
    bmi = float(request.form['bmi'])
    gender = request.form['gender'].strip().lower()
    ever_married = request.form['ever_married'].strip().lower()
    work_type = request.form['work_type'].strip().lower()
    residence_type = request.form['residence_type'].strip().lower()
    smoking_status = request.form['smoking_status'].strip().lower()

    # Cari data yang sesuai di dataset
    result = data[
        (data['age'] == age) &
        (data['avg_glucose_level'] == avg_glucose_level) &
        (data['bmi'] == bmi) &
        (data['gender'].str.lower() == gender) &
        (data['ever_married'].str.lower() == ever_married) &
        (data['work_type'].str.lower() == work_type) &
        (data['residence_type'].str.lower() == residence_type) &
        (data['smoking_status'].str.lower() == smoking_status)
    ]

    if not result.empty:
        prediction = result.iloc[0]['stroke']
    else:
        prediction = 'Data tidak ditemukan'

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)