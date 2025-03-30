import pandas as pd
import streamlit as st
import joblib  # To load the pre-trained model

# Load the trained model for predictions
@st.cache
def load_trained_model():
    return joblib.load('mental_health_model.pkl')  # Path to your pre-trained .pkl model

# Main dashboard layout
st.title('Mental Health Risk Prediction')

# Display a form to take user inputs for prediction
st.header('Predict Mental Health Risk')

with st.form(key='prediction_form'):
    # Collect user input for each feature used in the model
    self_employed = st.selectbox('Are you self-employed?', [0, 1])
    employer_mh_benefits = st.selectbox('Does your employer provide mental health benefits?', [0, 1])
    mh_coverage_options = st.selectbox('Do you know the options for mental health care available under your employer-provided coverage?', [0, 1])
    employer_resources = st.selectbox('Does your employer offer resources to learn more about mental health concerns and options for seeking help?', [0, 1])
    comfortable_with_coworkers = st.selectbox('Would you feel comfortable discussing a mental health disorder with your coworkers?', [0, 1])
    comfortable_with_supervisor = st.selectbox('Would you feel comfortable discussing a mental health disorder with your direct supervisor(s)?', [0, 1])
    think_negative_consequences = st.selectbox('Do you think that discussing a mental health disorder with your employer would have negative consequences?', [0, 1])
    had_mental_health_disorder = st.selectbox('Have you had a mental health disorder in the past?', [0, 1])
    current_mental_disorder = st.selectbox('Do you currently have a mental health disorder?', [0, 1])
    sought_treatment = st.selectbox('Have you sought treatment for mental health concerns?', [0, 1])
    productivity_affected = st.selectbox('Do you believe your productivity is ever affected by a mental health issue?', [0, 1])
    age = st.number_input('What is your age?', min_value=18, max_value=100, value=30)
    gender = st.selectbox('What is your gender?', ['Male', 'Female', 'Other'])
    know_resources = st.selectbox('Do you know local or online resources to seek help for a mental health disorder?', [0, 1])

    # When the form is submitted, make a prediction
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        model = load_trained_model()  # Load the pre-trained model

        # Construct the feature vector for the prediction
        input_data = pd.DataFrame({
            'Are you self-employed?': [self_employed],
            'employer_mh_benefits': [employer_mh_benefits],
            'Do you know the options for mental health care available under your employer-provided coverage?': [mh_coverage_options],
            'Does your employer offer resources to learn more about mental health concerns and options for seeking help?': [employer_resources],
            'Would you feel comfortable discussing a mental health disorder with your coworkers?': [comfortable_with_coworkers],
            'Would you feel comfortable discussing a mental health disorder with your direct supervisor(s)?': [comfortable_with_supervisor],
            'Do you think that discussing a mental health disorder with your employer would have negative consequences?': [think_negative_consequences],
            'Have you had a mental health disorder in the past?': [had_mental_health_disorder],
            'current_mental_disorder': [current_mental_disorder],
            'sought_treatment': [sought_treatment],
            'Do you believe your productivity is ever affected by a mental health issue?': [productivity_affected],
            'age': [age],
            'gender': [gender],  # Gender must be encoded before prediction
            'Do you know local or online resources to seek help for a mental health disorder?': [know_resources]
        })

        # Ensure the model's expected feature columns are included and in the correct order
        expected_features = [
            'Are you self-employed?', 'employer_mh_benefits',
            'Do you know the options for mental health care available under your employer-provided coverage?',
            'Does your employer offer resources to learn more about mental health concerns and options for seeking help?',
            'Would you feel comfortable discussing a mental health disorder with your coworkers?',
            'Would you feel comfortable discussing a mental health disorder with your direct supervisor(s)?',
            'Do you think that discussing a mental health disorder with your employer would have negative consequences?',
            'Have you had a mental health disorder in the past?',
            'current_mental_disorder', 'sought_treatment',
            'Do you believe your productivity is ever affected by a mental health issue?',
            'age', 'gender',
            'Do you know local or online resources to seek help for a mental health disorder?'
        ]

        # Reindex the input data to match the order of the expected features
        input_data = input_data[expected_features]

        # Gender encoding (same encoding as in training)
        gender_map = {'Male': 0, 'Female': 1, 'Other': 2}  # Assuming these were the values used in training
        input_data['gender'] = input_data['gender'].map(gender_map)

        # Check if all features are present in the input
        if input_data.isnull().any().any():
            st.error("There are missing values in your input. Please ensure all fields are filled.")
        else:
            # Predict the target (mental health risk)
            prediction = model.predict(input_data)

            # Display the prediction result
            if prediction == 1:
                st.write('You are at risk of mental health concerns.')
            else:
                st.write('You are not at risk of mental health concerns.')
