

import time
from book_sync_version import sync_book_main
from pokemon_sync_version import sync_pokemon_main


def run_both_sync():
    print('running both sync')
    sync_book_main()
    sync_pokemon_main()
        

# start_time = time.time()
# run_both_sync()
# time_difference = time.time() - start_time
# print(f'Total scraping time: %.2f seconds.' % time_difference)