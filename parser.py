import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout
from config import TIMEOUT, headers
from bs4 import BeautifulSoup

#response=requests.get(url, headers=headers, timeout=TIMEOUT)
#print(response.status_code)


def fetch_page(base_url, page):
    url = base_url.format(page)
    if page==1:
        url = "https://blog.python.org/blog/"
    print(f"Парсим страницу: {page}: {url}")

    # запрос 
    try: 
        response=requests.get(url, headers=headers, timeout=TIMEOUT)
        response.raise_for_status()
        data=response.text

    # ловим исключения
    except HTTPError as httper:
        print(f"Ошибка HTTP: {httper}")    
    
    except ConnectionError as ce:
        print(f"Ошибка соединения: {ce}")

    except Timeout as t:
        print(f"Превышено время ожидания: {t}")

    except Exception as e:
        print(f"Другая ошибка: {e}")
    else:
        return data

# извлечение информации - парсинг
def parse_page(data):
    soup=BeautifulSoup(data, "lxml")
    articles = soup.find_all("article", class_="post-card group relative px-5 py-4")
    
    news_list=[]

    for article in articles:

        article_link=article.find("a", class_="block").get("href")
        article_title=article.find("a", class_="block").find("h3").text
        article_author=article.find("div", class_="mt-1 flex flex-wrap items-center gap-x-2 gap-y-0.5 text-xs text-zinc-500 dark:text-zinc-400").find("a").text
        article_date=article.find("div", class_="mt-1 flex flex-wrap items-center gap-x-2 gap-y-0.5 text-xs text-zinc-500 dark:text-zinc-400").find("time").text
    
        news_list.append({
            "title": article_title,
            "link": article_link,
            "author": article_author,
            "date": article_date
            })

    return news_list

