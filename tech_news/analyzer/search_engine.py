from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    return [(new['title'], new['url']) for new in search_news(
        {'title': {'$regex': title, '$options': 'i'}})]


# Requisito 8
def search_by_date(date):
    try:
        date = datetime.fromisoformat(date).strftime('%d/%m/%Y')
        return [(new['title'], new['url'])
                for new in search_news({'timestamp': date})]
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
