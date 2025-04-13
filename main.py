import json
from scrapers.bbc_scraper import BBCLatinAmericaScraper
from preprocessing.main_preprocess import ArticlePreprocessor
from summarization.textSummarization import TextSummarization

def main():
    print("Starting scraping...")
    scraper = BBCLatinAmericaScraper()
    scraper.run()

    print("Starting pre-processing...")
    preprocessor = ArticlePreprocessor()
    preprocessor.preprocess()

    print("Starting summarization...")
    summarizer = TextSummarization()

    with open('data/processed/bbc_cleaned_news.json', 'r', encoding='utf-8') as f:
        articles = json.load(f)

    summarized_articles = []
    for article in articles:
        full_text = " ".join(article['sentences'])
        summaries = summarizer.summarize_article(full_text)
        
        summarized_articles.append({
            'title': article['title'],
            'summary_extractive': summaries['summary_extractive'],
            'summary_abstractive': summaries['summary_abstractive']
        })

    with open('data/processed/bbc_summarized_news.json', 'w', encoding='utf-8') as f:
        json.dump(summarized_articles, f, ensure_ascii=False, indent=4)

    print("Pipeline successfully completed!")

if __name__ == '__main__':
    main()