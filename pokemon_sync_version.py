import csv
import json
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

csv_reader = ['https://scrapeme.live/shop/Bulbasaur/', 'https://scrapeme.live/shop/Ivysaur/', 'https://scrapeme.live/shop/Venusaur/', 'https://scrapeme.live/shop/Charmander/']

def save_product(pokemon_name, pokemon_desc):
    json_file_name = pokemon_name.replace(" ", "_")
    with open(f"data/{json_file_name}.json", "w") as pokemon_file:
        json.dump(pokemon_desc, pokemon_file)
    print(f'{pokemon_name} saved')


def scrape(url):
    print(f'fetching url: {url}')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    print('eepy')
    time.sleep(0.5)
    body = driver.page_source
    soup = BeautifulSoup(body, "html.parser")
    driver.quit()

    pokemon_name = soup.select_one('.product').h1.text
    pokemon_desc = soup.select_one('#tab-description').text
    save_product(pokemon_name, pokemon_desc)


def sync_pokemon_main():
    start_time = time.time()

    print("Saving the output of extracted information sync")
    for csv_row in csv_reader:
        scrape(csv_row)

    time_difference = time.time() - start_time
    print(f"Scraping time: %.2f seconds." % time_difference)


# sync_pokemon_main()
