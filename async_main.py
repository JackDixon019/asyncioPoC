import asyncio
import time
from book_asyncer import book_main
from pokemon_asyncer import poke_main

async def run_both():
    print('running both async')
    await asyncio.gather(
        poke_main(),
        book_main()
    )

# start_time = time.time()
# asyncio.run(run_both())
# time_difference = time.time() - start_time
# print(f'in async main: Total scraping time: %.2f seconds.' % time_difference)