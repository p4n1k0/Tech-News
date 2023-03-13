import requests
import time
import parsel


# Requisito 1
def fetch(url):
    HEADER = {"user-agent": "Fake user-agent"}
    time.sleep(1)
    try:
        response = requests.get(url, headers=HEADER, timeout=3)
        if response.status_code == 200:
            return response.text
    except requests.exceptions.RequestException:
        return None


# Requisito 2
def scrape_updates(html_content):
    return parsel.Selector(html_content).css(
       '.cs-overlay-link::attr(href)').getall()


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
    """Seu código deve vir aqui"""
