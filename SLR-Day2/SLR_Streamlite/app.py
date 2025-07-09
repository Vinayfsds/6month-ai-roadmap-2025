import streamlit as st
import pickle
import numpy as np
#from sklearn.linear_model import LinearRegression  # Add this import to resolve the error

# Load the pre-trained model
model = pickle.load(open(r'C:\sample\Resume Projects\AVSCODE\SLR_Streamlite\linear_regression_model.pkl', 'rb'))

st.title("Simple Linear Regression Prediction App")
st.write("This app predicts the target variable based on the input features using a pre-trained linear regression model.")
# Input features
years_of_experience = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, step=0.1)
# Predict button
if st.button("Predict Salary"):
    # Prepare the input data for prediction
    experience_input = np.array([[years_of_experience]])
    
    # Make prediction using the loaded model
    prediction = model.predict(experience_input)
    
    # Display the prediction result
    st.success(f"The predicted value is: {prediction[0]:.2f}")
# Display additional information
st.write("This app uses a simple linear regression model trained on a dataset of salaries based on years of experience.")