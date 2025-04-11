import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict

nltk.download('punkt')
nltk.download('stopwords')

class ExtractiveSummarizer:
    def __init__(self, language='english'):
        self.stop_words = set(stopwords.words(language))

    def summarize(self, text: str, num_sentences: int = 3) -> list[str]:
        sentences = sent_tokenize(text)
        if len(sentences) <= num_sentences:
            return sentences

        word_freq = defaultdict(int)
        for word in word_tokenize(text.lower()):
            if word.isalnum() and word not in self.stop_words:
                word_freq[word] += 1

        sentence_scores = {}
        for sentence in sentences:
            words = word_tokenize(sentence.lower())
            score = sum(word_freq[word] for word in words if word in word_freq)
            sentence_scores[sentence] = score

        ranked = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
        return ranked[:num_sentences]