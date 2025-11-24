import nltk
nltk.download('stopwords')

from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = BeautifulSoup(text, "html.parser").get_text()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r"[^a-zA-Z0-9\- ]", " ", text)
    text = text.lower()
    words = [word for word in text.split() if word not in stop_words]
    return " ".join(words)
