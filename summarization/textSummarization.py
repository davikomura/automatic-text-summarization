from summarization.extractive import ExtractiveSummarizer
from summarization.abstractive import AbstractiveSummarizer

class TextSummarization:
    def __init__(self):
        self.extractive = ExtractiveSummarizer()
        self.abstractive = AbstractiveSummarizer()

    def summarize_article(self, text: str, max_abs_len: int = 160, min_abs_len: int = 30, num_sentences_ext: int = 5) -> dict:
        extractive_summary = self.extractive.summarize(text, num_sentences=num_sentences_ext)
        abstractive_summary = self.abstractive.summarize(text, max_length=max_abs_len, min_length=min_abs_len)
        return {
            'summary_extractive': " ".join(extractive_summary),
            'summary_abstractive': abstractive_summary
        }