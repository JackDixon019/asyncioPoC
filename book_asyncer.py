import asyncio
import csv
import json
import time
from selenium_driverless import webdriver
from selenium_driverless.types.by import By
from bs4 import BeautifulSoup


csv_reader = ['http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html', 'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html', 'http://books.toscrape.com/catalogue/soumission_998/index.html', 'http://books.toscrape.com/catalogue/sharp-objects_997/index.html']


async def save_product(book_name, product_info):
    json_file_name = book_name.replace(' ', '_')
    with open(f'data/{json_file_name}.json', 'w') as book_file:
        json.dump(product_info, book_file)
    print(f'{book_name} saved')



async def scrape(url):
    print(f'fetching url: {url}')
    # initiate driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    
    async with webdriver.Chrome(options=options) as driver:
        await driver.get(url)
        body = await driver.page_source
        soup = BeautifulSoup(body, 'html.parser')
        await driver.quit()
        book_name = soup.select_one('.product_main').h1.text
        rows = soup.select('.table.table-striped tr')
        product_info = {row.th.text: row.td.text for row in rows}
        await save_product(book_name, product_info)


async def book_main():
    start_time = time.time()

    print('Saving the output of extracted information')
    async with asyncio.TaskGroup() as tg:
        for csv_row in csv_reader:
            tg.create_task(scrape(csv_row))

    time_difference = time.time() - start_time
    print(f'Scraping time: %.2f seconds.' % time_difference)


# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())


