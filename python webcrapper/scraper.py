import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://books.toscrape.com/catalogue/"
START_URL = BASE_URL + "page-1.html"
MAX_PAGES = 5
OUTPUT_FILE = "books.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_page(url):
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")


def parse_books(soup):
    books = []

    for article in soup.find_all("article", class_="product_pod"):
        title = article.h3.a["title"]
        price = article.find("p", class_="price_color").text.strip()

        rating_word = article.find("p", class_="star-rating")["class"][1]
        rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        rating = rating_map.get(rating_word, 0)

        availability = article.find("p", class_="instock availability").text.strip()

        books.append([title, price, rating, availability])

    return books


def get_next_page(soup):
    next_btn = soup.find("li", class_="next")
    if next_btn:
        return BASE_URL + next_btn.a["href"]
    return None


def save_csv(data):
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Price", "Rating", "Availability"])
        writer.writerows(data)


def main():
    url = START_URL
    all_books = []
    page = 1

    while url and page <= MAX_PAGES:
        print(f"Scraping page {page}")

        soup = get_page(url)
        all_books += parse_books(soup)
        url = get_next_page(soup)

        page += 1

    print("Done:", len(all_books), "books found")
    save_csv(all_books)


if __name__ == "__main__":
    main()