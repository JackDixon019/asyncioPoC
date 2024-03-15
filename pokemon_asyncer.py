import asyncio
import csv
import json
import time
from selenium_driverless import webdriver
from selenium_driverless.types.by import By
from bs4 import BeautifulSoup


csv_reader = ['https://scrapeme.live/shop/Bulbasaur/', 'https://scrapeme.live/shop/Bulbasaursss/', 'https://scrapeme.live/shop/Ivysaur/', 'https://scrapeme.live/shop/Venusaur/', 'https://scrapeme.live/shop/Charmander/']


async def save_product(pokemon_name, pokemon_desc):
    json_file_name = pokemon_name.replace(' ', '_')
    with open(f'data/{json_file_name}.json', 'w') as pokemon_file:
        json.dump(pokemon_desc, pokemon_file)
    print(f'{pokemon_name} saved')



async def scrape(url):
    print(f'fetching url: {url}')
    # initiate driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    
    async with webdriver.Chrome(options=options) as driver:
        try:
            await driver.get(url)
            body = await driver.page_source
            soup = BeautifulSoup(body, 'html.parser')
            await driver.quit()
            pokemon_name = soup.select_one('.product').h1.text
            pokemon_desc = soup.select_one('#tab-description').text
            await save_product(pokemon_name, pokemon_desc)
            return pokemon_name
        except:
            print(f'{url} could not be scraped')
            pass
        finally:
            await driver.quit()


async def poke_main():
    start_time = time.time()

    print('Saving the output of extracted information async')
    result = []

    # creates promise-like objects - "coroutines"
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(scrape(csv_row)) for csv_row in csv_reader]

    for pokemon_name in [task.result() for task in tasks if task.result() != None]:
        print(pokemon_name)

    # NB: this can cause issues where python drops a task without an assignment
    # more of an issue with more tasks
    # print(await asyncio.gather(*[scrape(csv_row) for csv_row in csv_reader]))

    time_difference = time.time() - start_time
    print(f'Scraping time: %.2f seconds.' % time_difference)


# loop = asyncio.get_event_loop()
# loop.run_until_complete(poke_main())


