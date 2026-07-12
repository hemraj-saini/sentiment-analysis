import spacy
import string
import joblib
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords


stop_words=set(stopwords.words('english'))
nlp = spacy.load("en_core_web_sm",disable=["parser", "ner"])

def lowercase(text):
    
    return text.lower()

def remove_html(text):

    return BeautifulSoup(text,'html.parser').get_text()

def remove_punctuation(text):

    return text.translate(str.maketrans('', '',string.punctuation))

def remove_special_char(text):

    return re.sub(r'[^a-zA-Z0-9\s]','',text)

def remove_extra_spaces(text):

    return re.sub(r'\s+',' ',text).strip()

def remove_stopword(text):

    words=text.split()

    words=[word for word in words if word not in stop_words]
    
    return " ".join(words)

def lemmatize_text(text):

    doc = nlp(text)

    return " ".join(token.lemma_ for token in doc)


def preprocess(text):

    text=lowercase(text)
    
    text=remove_html(text)
    
    text=remove_punctuation(text)
    
    text=remove_special_char(text)
    
    text=remove_extra_spaces(text)
    
    text=remove_stopword(text)
    
    text=lemmatize_text(text)

    return text

