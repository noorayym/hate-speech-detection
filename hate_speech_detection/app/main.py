import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Loading the tokenizer and max_sequence_length
tokenizer_path = '/Users/nuraiym/PycharmProjects/hate_speech_detection/app/trained_model/tokenizer.pkl'
max_sequence_length = 100

with open(tokenizer_path, 'rb') as handle:
    tokenizer = pickle.load(handle)

class_indices = {0: 'Hate Speech', 1: 'Offensive Language', 2: 'Neither'}

def preprocess_text(text):
    sequences = tokenizer.texts_to_sequences([text])
    padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length)
    return padded_sequences

def predict_text_class(model, text, class_indices):
    preprocessed_text = preprocess_text(text)
    predictions = model.predict(preprocessed_text)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    predicted_class = class_indices[predicted_class_index]
    return predicted_class

# Streamlit app
st.title('Hate Speech Classifier')
st.write('Enter a tweet and classify it as hate speech, offensive language, or neither.')

# User input
user_input = st.text_input('Enter your tweet here')

# Load the trained model
model_path = '/Users/nuraiym/PycharmProjects/hate_speech_detection/app/trained_model/hate_speech_model.h5'
try:
    model = load_model(model_path)
except Exception as e:
    st.error(f"Error loading model: {e}")
    model = None

if st.button('Classify'):
    if user_input:
        if model is not None:
            try:
                prediction = predict_text_class(model, user_input, class_indices)
                st.write(f'The tweet is classified as: {prediction}')
            except Exception as e:
                st.error(f"Error during prediction: {e}")
        else:
            st.error("Model could not be loaded. Please check the model file.")
    else:
        st.write('Please enter a tweet to classify.')
