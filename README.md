# Movie Review Sentiment Analysis

This project is a Machine Learning and NLP application that predicts whether an IMDb movie review is **Positive** or **Negative**. The application performs text preprocessing, converts the text into TF-IDF features, and uses a trained machine learning model to predict the sentiment. A simple Streamlit interface is provided for users to test reviews in real time.

## Live Demo

https://sentiment-analysis-9g592iab9ah4rm7xg2bkwz.streamlit.app/

## Features

- Predict sentiment of movie reviews
- Text preprocessing using NLP
- Stopword removal and lemmatization
- TF-IDF feature extraction
- Interactive Streamlit web application

## Technologies Used

- Python
- Scikit-learn
- Streamlit
- NLTK
- spaCy
- BeautifulSoup
- Pandas
- NumPy
- Joblib

## Project Structure

```text
sentiment-analysis/
│── app.py
│── preprocessing.py
│── requirements.txt
│── models/
│   ├── model.pkl
│   └── tfidf.pkl
└── README.md
```

## Installation

```bash
git clone https://github.com/hemraj-saini/sentiment-analysis.git

cd sentiment-analysis

pip install -r requirements.txt

streamlit run app.py
```

## How It Works

1. Enter a movie review.
2. The review is cleaned using NLP preprocessing.
3. TF-IDF transforms the text into numerical features.
4. The trained model predicts the sentiment.
5. The result is displayed as Positive or Negative.

## Author

Hemraj Saini

GitHub: https://github.com/hemraj-saini
