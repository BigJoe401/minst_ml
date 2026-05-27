import streamlit as st
from utils import load_model, predict_digit

model = load_model()

st.title("MNIST Digit Classifier")

uploaded_file = st.file_uploader("Upload a digit image")

if uploaded_file:
    digit, confidence = predict_digit(model, uploaded_file)

    st.write(f"Predicted digit: {digit}")
    st.write(f"Confidence: {confidence:.2%}")