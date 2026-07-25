from parser import fetch_page, parse_page
from config import base_url
import time
import csv

all_news=[] # собираю вместе новости с каждой страницы

if __name__ == "__main__":
    for page in range(1,6): # буду парсить только первые 5 страниц
        html=fetch_page(base_url, page) 
        if html:
            page_news=parse_page(html)
            all_news.extend(page_news)
            time.sleep(2) # задержка, чтобы parser не забанили

    # сохраняю информацию в CSV файл
    with open("news.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=['date', 'title', 'author', 'link'])
        writer.writeheader()
        writer.writerows(all_news)

