from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news_found = search_news({"title": {"$regex": title, "$options": "i"}})
    news_list = []
    for new in news_found:
        new_tuple = (new["title"], new["url"])
        news_list.append(new_tuple)
    return news_list


# Requisito 7
def search_by_date(date):
    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
        news_found = search_news({"timestamp": {"$eq": formatted_date}})
        news_list = []
        for new in news_found:
            new_tuple = (new["title"], new["url"])
            news_list.append(new_tuple)
        return news_list
    except ValueError:
        raise ValueError("Data inválida")


def search_by_tag(tag):
    news_found = search_news(
        {"tags": {"$elemMatch": {"$regex": tag, "$options": "i"}}}
    )
    news_list = []
    for new in news_found:
        new_tuple = (new["title"], new["url"])
        news_list.append(new_tuple)
    return news_list


# Requisito 9
def search_by_category(category):
    news_found = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    news_list = []
    for new in news_found:
        new_tuple = (new["title"], new["url"])
        news_list.append(new_tuple)
    return news_list
