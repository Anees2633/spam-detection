import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')
nltk.download('punkt')

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

# Load saved model and vectorizer
model = pickle.load(open('spam_model.pkl', 'rb'))
tfidf = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

def clean_text(message):
    message = message.lower()
    message = re.sub('[^a-z]', ' ', message)
    words = message.split()
    words = [ps.stem(word) for word in words if word not in stop_words]
    return ' '.join(words)

# App title
st.title("📧 Spam Email Detector")
st.write("Enter a message below to check if it is spam or not.")

# Text input box
user_input = st.text_area("Enter your message here:", height=150)

# Predict button
if st.button("Check Message"):
    if user_input.strip() == "":
        st.warning("Please enter a message first!")
    else:
        # Clean and transform input
        cleaned = clean_text(user_input)
        vectorized = tfidf.transform([cleaned])
        prediction = model.predict(vectorized)[0]

        # Show result
        if prediction == 1:
            st.error("🚨 This message is SPAM!")
        else:
            st.success("✅ This message is NOT spam!")