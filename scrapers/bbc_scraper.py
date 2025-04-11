import os
import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup

BASE_URL = 'https://www.bbc.com/news/world/latin_america'

DATA_DIR = os.path.join(os.getcwd(), 'data', 'raw')
os.makedirs(DATA_DIR, exist_ok=True)

def fetch_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)
    print(f"Status Code for {url}: {response.status_code}")
    if response.status_code == 200:
        return response.text
    else:
        print(f"Access error {url}: Code {response.status_code}")
        return None

def parse_article_links(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    
    alaska_section_div = soup.find('div', {'data-testid': 'alaska-section'})
    
    article_links = []
    
    if alaska_section_div:
        for a_tag in alaska_section_div.find_all('a', {'data-testid': 'internal-link'}, href=True):
            href = a_tag['href']
            
            if href.startswith('/news/articles/'):
                full_url = f"https://www.bbc.com{href}"
                article_links.append(full_url)
    
    return article_links

def fetch_article_content(article_url):
    page_html = fetch_page(article_url)
    if not page_html:
        return None

    soup = BeautifulSoup(page_html, 'html.parser')
    title_tag = soup.find('h1')
    date_tag = soup.find('time')
    content_tags = soup.find_all('div', {'data-component': 'text-block'})

    if title_tag and date_tag and content_tags:
        title = title_tag.get_text(strip=True)
        date = date_tag.get('datetime', '').strip()

        content = ' '.join(
            p.get_text(strip=True)
            for div in content_tags
            for p in div.find_all('p')
        )

        return {
            'url': article_url,
            'title': title,
            'date': date,
            'content': content
        }
    else:
        print(f"Information missing from the article: {article_url}")
        return None

def save_to_json(data, filename_prefix):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"{filename_prefix}_{timestamp}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    page_html = fetch_page(BASE_URL)
    if not page_html:
        return

    article_links = parse_article_links(page_html)
    if not article_links:
        print("No article links found.")
        return

    articles = []
    for url in article_links:
        article_data = fetch_article_content(url)
        if article_data:
            articles.append(article_data)

    if articles:
        save_to_json(articles, os.path.join(DATA_DIR, 'bbc_latin_america_news'))
        print(f"{len(articles)} successfully saved articles.")
    else:
        print("No articles collected.")

if __name__ == '__main__':
    main()