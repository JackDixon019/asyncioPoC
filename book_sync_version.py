import csv
import json
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

csv_reader = [
    "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
    "http://books.toscrape.com/catalogue/soumission_998/index.html",
    "http://books.toscrape.com/catalogue/sharp-objects_997/index.html",
]


def save_product(book_name, product_info):
    json_file_name = book_name.replace(" ", "_")
    with open(f"data/{json_file_name}.json", "w") as book_file:
        json.dump(product_info, book_file)
    print(f'{book_name} saved')


def scrape(url):
    print(f'fetching url: {url}')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(0.5)
    body = driver.page_source
    soup = BeautifulSoup(body, "html.parser")
    driver.quit()
    book_name = soup.select_one(".product_main").h1.text
    rows = soup.select(".table.table-striped tr")
    product_info = {row.th.text: row.td.text for row in rows}
    save_product(book_name, product_info)


def sync_book_main():
    start_time = time.time()

    print("Saving the output of extracted information")
    for csv_row in csv_reader:
        scrape(csv_row)

    time_difference = time.time() - start_time
    print(f"Scraping time: %.2f seconds." % time_difference)


# sync_book_main()
