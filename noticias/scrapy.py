# news/scrape.py
import requests
from bs4 import BeautifulSoup

def scrape_g1_news():
    url = 'https://g1.globo.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    news_list = []
    headlines = soup.find_all('div', class_='bastian-feed-item')
    
    for headline in headlines:
        news = {}
        news['title'] = headline.find('a', class_='feed-post-link').text.strip()
        news['link'] = headline.find('a', class_='feed-post-link')['href']
        news['image'] = headline.find('img')['src']
        news_list.append(news)
    
    return news_list
