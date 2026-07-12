import streamlit as st
import joblib
import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

from preprocessing import preprocess

# Load Model
model = joblib.load("models/model.pkl")
tfidf = joblib.load("models/tfidf.pkl")

st.set_page_config(
    page_title="Movie Sentiment Analysis"
)

st.title(" IMDb Movie Review Sentiment Analysis")

st.write("Enter a movie review and predict whether it is Positive or Negative.")

review = st.text_area("Movie Review")

if st.button("Predict"):

    if review.strip() == "":
        st.warning("Please enter a review.")

    else:

        review = preprocess(review)

        X = tfidf.transform([review])

        prediction = model.predict(X)[0]

        if prediction == 1:
            st.success(" Positive Review")

        else:
            st.error("Negative Review")

from preprocessing import preprocess

# Load Model
model = joblib.load("models/model.pkl")
tfidf = joblib.load("models/tfidf.pkl")

st.set_page_config(
    page_title="Movie Sentiment Analysis"
)

st.title(" IMDb Movie Review Sentiment Analysis")

st.write("Enter a movie review and predict whether it is Positive or Negative.")

review = st.text_area("Movie Review")

if st.button("Predict"):

    if review.strip() == "":
        st.warning("Please enter a review.")

    else:

        review = preprocess(review)

        X = tfidf.transform([review])

        prediction = model.predict(X)[0]

        if prediction == 1:
            st.success(" Positive Review")

        else:
            st.error("Negative Review")
