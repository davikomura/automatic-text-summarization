from scrapers.bbc_scraper import BBCLatinAmericaScraper
from preprocessing.main_preprocess import ArticlePreprocessor

def main():
    print("Starting scraping...")
    scraper = BBCLatinAmericaScraper()
    scraper.run()

    print("Starting pre-processing...")
    preprocessor = ArticlePreprocessor()
    preprocessor.preprocess()

    print("Pipeline successfully completed!")

if __name__ == '__main__':
    main()