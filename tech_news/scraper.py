import requests
import time
from parsel import Selector
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
    response = parsel.Selector(html_content).css('.next::attr(href)').get()
    if not response:
        return None
    return response


# Requisito 4
def scrape_news(html_content):
    return {
        'url': parsel.Selector(html_content).css(
            '.pk-share-buttons-wrap').attrib['data-share-url'],
        'title': parsel.Selector(html_content).css(
            '.entry-title::text').get().strip('\xa0'),
        'timestamp': parsel.Selector(html_content).css(
            '.meta-date::text').get(),
        'writer': parsel.Selector(html_content).css('.n::text').get(),
        'reading_time': int(parsel.Selector(html_content).css(
            '.meta-reading-time::text').get().split(' ')[0]),
        'summary': parsel.Selector(html_content).css(
            '.entry-content p').xpath('string()').get().strip(),
        'category': parsel.Selector(html_content).css('.label::text').get()
    }


# Requisito 5
def get_tech_news(amount):
    url = 'https://blog.betrybe.com/'
    list = []
    while len(list) < amount:
        response = fetch(url)
        list += scrape_updates(response)
        url = scrape_next_page_link(response)
    news = [scrape_news(fetch(link))
            for link in list[:amount]]
    create_news(news)
    return news
