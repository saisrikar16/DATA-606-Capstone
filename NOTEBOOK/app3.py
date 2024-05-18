import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the trained model
model_file = 'random_forest_regressor_model.pkl'
with open(model_file, 'rb') as file:
    model = pickle.load(file)

# Function to predict insurance claim amount
def predict_claim(features, model):
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    return prediction

# Streamlit 
def main():
    st.title('Health Insurance Claim Prediction')
    st.write('Enter the following details to predict the insurance claim amount:')

    # Input fields
    sum_insured = st.number_input('Sum Insured')
    age = st.slider('Age', 18, 100, 25)
    sex = st.radio('Sex', ('Male', 'Female'))
    weight = st.number_input('Weight (kg)')
    bmi = st.number_input('BMI (Body Mass Index)')
    hereditary_diseases = st.radio('Hereditary Diseases', ('Yes', 'No'))
    no_of_dependents = st.slider('Number of Dependents', 0, 10, 0)
    smoker = st.radio('Smoker', ('Yes', 'No'))
    city = st.text_input('City')
    bloodpressure = st.number_input('Blood Pressure')
    diabetes = st.radio('Diabetes', ('Yes', 'No'))
    regular_ex = st.radio('Regular Exercise', ('Yes', 'No'))
    job_title = st.text_input('Job Title')
    age_group = st.selectbox('Age Group', ['Youth', 'Adult', 'Elderly'])
    bmi_category = st.selectbox('BMI Category', ['Underweight', 'Normal', 'Overweight', 'Obese'])
    bp_category = st.selectbox('Blood Pressure Category', ['Normal', 'Prehypertension', 'Hypertension'])
    dependents_group = st.selectbox('Dependents Group', ['None', 'Few', 'Many'])

    # Prediction
    if st.button('Predict Claim'):
        # Convert categorical features to binary using LabelEncoder
        label_encoder = LabelEncoder()
        sex = label_encoder.fit_transform([sex])[0]
        hereditary_diseases = label_encoder.fit_transform([hereditary_diseases])[0]
        smoker = label_encoder.fit_transform([smoker])[0]
        diabetes = label_encoder.fit_transform([diabetes])[0]
        city = label_encoder.fit_transform([city])[0]
        job_title = label_encoder.fit_transform([job_title])[0]
        regular_ex = label_encoder.fit_transform([regular_ex])[0]
        age_group = label_encoder.fit_transform([age_group])[0]
        bmi_category = label_encoder.fit_transform([bmi_category])[0]
        bp_category = label_encoder.fit_transform([bp_category])[0]
        dependents_group = label_encoder.fit_transform([dependents_group])[0]

        # Generate features
        features = [sum_insured, age, sex, weight, bmi, hereditary_diseases, no_of_dependents, smoker, city, bloodpressure,
                    diabetes, regular_ex, job_title, age_group, bmi_category, bp_category, dependents_group]

        prediction = predict_claim(features, model)
        st.write(f'Predicted Claim Amount: {prediction[0]}')

if __name__ == '__main__':
    main()
