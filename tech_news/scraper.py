import requests
import time
from parsel import Selector
import re
from .database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=2
        )
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    url_list = selector.css("h2.entry-title a::attr(href)").getall()
    return url_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css("a.next::attr(href)").get()
    return next_page


# Requisito 4
def scrape_news(html_content):    
    return {
        'url': Selector(html_content).css(
            '.pk-share-buttons-wrap').attrib['data-share-url'],
        'title': Selector(html_content).css(
            '.entry-title::text').get().strip('\xa0'),
        'timestamp': Selector(html_content).css(
            '.meta-date::text').get(),
        'writer': Selector(html_content).css('.n::text').get(),
        'reading_time': int(Selector(html_content).css(
            '.meta-reading-time::text').get().split(' ')[0]),
        'summary': Selector(html_content).css(
            '.entry-content p').xpath('string()').get().strip(),
        'category': Selector(html_content).css('.label::text').get()
    }


# Requisito 5
def get_tech_news(amount):
    base_url = "https://blog.betrybe.com/"
    html = fetch(base_url)
    next_page_link = scrape_next_page_link(html)
    urls_list = scrape_updates(html)
    news_list = []

    while len(urls_list) < amount:
        next_html = fetch(next_page_link)
        next_page_link = scrape_next_page_link(next_html)
        next_page_news = scrape_updates(next_html)
        urls_list.extend(next_page_news)

    for url in urls_list[0:amount]:
        article_html = fetch(url)
        article_content = scrape_news(article_html)
        news_list.append(article_content)

    create_news(news_list)
    return news_list
