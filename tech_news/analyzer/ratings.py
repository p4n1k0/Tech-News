from collections import Counter
from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    result = []
    news = find_news()
    categories_list = Counter([new["category"] for new in news])
    for cate in sorted(
        categories_list.items(), key=lambda item: (-item[1], item[0])
    ):
        result.append(cate[0])
    return result
