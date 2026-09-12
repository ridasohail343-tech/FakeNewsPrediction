import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download("stopwords")
model = pickle.load(open("model.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))
stop_words = set(stopwords.words("english"))
ps = PorterStemmer()
def preprocess(text):
    text = text.lower()
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )
    words = text.split()
    new_words = []
    for word in words:
        if word not in stop_words:
            new_words.append(word)
    stemmed_words = []
    for word in new_words:
        stemmed_words.append(ps.stem(word))
    return " ".join(stemmed_words)

st.title("Fake News Detection")

text = st.text_area("Enter news text")

if st.button("Predict"):

    if text:

        processed_text = preprocess(text)

        text_tfidf = tfidf.transform([processed_text])

        prediction = model.predict(text_tfidf)[0]

        if prediction == 0:
            st.error("FAKE News")
        else:
            st.success("REAL News")

    else:
        st.warning("Please enter news text")