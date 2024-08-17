# Hate Speech Classifier

## Overview

The Hate Speech Classifier project provides a Streamlit web application for classifying tweets into three categories: Hate Speech, Offensive Language, and Neither. This project utilizes a deep learning model trained to detect hate speech and offensive language from textual data, allowing users to easily input tweets and receive real-time classification results. The model is built and trained using a Jupyter Notebook, and the Streamlit application provides an intuitive interface for interaction.
## Directories and Files Description

- **`app/`**: Contains the Streamlit application and the trained model.
  - **`trained_model/`**: Directory with the trained model and tokenizer files.
    - **`hate_speech_model.h5`**: The trained deep learning model.
    - **`tokenizer.pkl`**: Tokenizer for text preprocessing.
  - **`class_indices.json`**: Mapping of class indices to labels.
  - **`config.toml`**: Configuration file for Streamlit settings.
  - **`credentials.toml`**: File for credentials configuration.
  - **`main.py`**: Main script for the Streamlit application.
  - **`requirements.txt`**: List of Python dependencies.

- **`Hate.ipynb`**: Jupyter Notebook for training and building the model.
(Link: https://colab.research.google.com/drive/1yww1VsnNWAfBkMqgo-zV68K9ysyCY7aX?usp=sharing)
- **`labeled_data.csv`**: CSV file containing labeled data for training.
- **`LICENSE`**: License file for the project.

## Installation

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
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

## Model Training

The model is trained using the Jupyter Notebook `Hate.ipynb`. This notebook includes the following steps:

- Data loading and preprocessing
- Model architecture definition
- Model training
- Evaluation

## License

This project is licensed under the terms of the MIT License.
