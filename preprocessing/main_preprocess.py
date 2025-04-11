import os
import json
import glob
from .cleaner import TextCleaner
from .tokenizer import TextTokenizer

class ArticlePreprocessor:
    def __init__(self, raw_dir='data/raw', processed_path='data/processed/bbc_cleaned_news.json'):
        self.raw_dir = raw_dir
        self.processed_path = processed_path

        os.makedirs(os.path.dirname(self.processed_path), exist_ok=True)
        self.cleaner = TextCleaner()
        self.tokenizer = TextTokenizer()

    def get_latest_raw_file(self):
        files = glob.glob(os.path.join(self.raw_dir, 'bbc_latin_america_news_*.json'))
        if not files:
            raise FileNotFoundError("Nenhum arquivo JSON encontrado em data/raw.")
        latest_file = max(files, key=os.path.getmtime)
        return latest_file

    def preprocess(self):
        raw_path = self.get_latest_raw_file()
        
        with open(raw_path, 'r', encoding='utf-8') as f:
            raw_articles = json.load(f)

        processed_articles = []
        for article in raw_articles:
            cleaned = self.cleaner.clean(article['content'])
            sentences = self.tokenizer.tokenize_sentences(cleaned)
            processed_articles.append({
                'title': article['title'],
                'url': article['url'],
                'date': article['date'],
                'sentences': sentences
            })

        with open(self.processed_path, 'w', encoding='utf-8') as f:
            json.dump(processed_articles, f, ensure_ascii=False, indent=4)

        print(f"Processed {len(processed_articles)} articles. Saved to {self.processed_path}")