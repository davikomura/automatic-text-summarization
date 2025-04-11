import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from typing import List

def download_nltk_resources():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')

download_nltk_resources()

class TextTokenizer:
    def __init__(self, language: str = 'english'):
        self.stop_words = set(stopwords.words(language))

    def tokenize_sentences(self, text: str) -> List[str]:
        return sent_tokenize(text)

    def tokenize_words(self, text: str) -> List[str]:
        words = word_tokenize(text)
        return [word for word in words if word.lower() not in self.stop_words and word.isalnum()]