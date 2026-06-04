# 📚 Book Scraper

This is a simple Python project that scrapes book data from [books.toscrape.com](https://books.toscrape.com) and saves it into a CSV file.

I built this project to practice web scraping and understand how data extraction from websites works using Python.

---

## 🚀 What it does

This scraper:

* Visits the website automatically
* Collects book details like:

  * Title
  * Price
  * Rating
  * Availability
* Moves through multiple pages
* Saves everything into a CSV file

---

## 🛠️ Technologies used

* Python
* Requests
* BeautifulSoup
* CSV module

---

## ▶️ How to run it

1. Install the required libraries:

```bash
pip install requests beautifulsoup4
```

2. Run the script:

```bash
python scraper.py
```

3. After running, you’ll get a file called:

```
books.csv
```

---

## 📂 Output

The output file contains structured data like:

* Book Title
* Price
* Rating
* Stock status

---

## 💡 Why I made this

This project helped me understand:

* How websites are structured (HTML)
* How data can be extracted from web pages
* Basics of automation using Python

---

## ⚠️ Note

This scraper is only for learning purposes and works on a demo website made for practice.

---

## ✨ Future improvements

* Add database storage
* Export to Excel with formatting
* Build a simple UI for it
* Scrape more complex websites
