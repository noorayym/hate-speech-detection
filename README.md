# Hate Speech Classifier

## Overview

Three different approaches were used to detect hate speech and offensive language: logistic regression with TF-IDF, LSTM, and transformer-based model ELECTRA. The results of each model are provided. In addition, the Streamlit web application using LSTM was built for classifying tweets into three categories: Hate Speech, Offensive Language, and Neither.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/noorayym/hate-speech-detection
    cd hate-speech-detection
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required Python packages:**

    ```bash
    pip install -r app/requirements.txt
    ```

## Usage

1. **Run the Streamlit application:**

    ```bash
    streamlit run app/main.py
    ```

2. **Open your browser and navigate to `http://localhost:8501` to access the application.**

3. **Enter a tweet in the input box and click 'Classify' to see the classification result.**

## License

This project is licensed under the terms of the MIT License.
