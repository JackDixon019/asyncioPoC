import asyncio
import time

from async_main import run_both
from sync_main import run_both_sync


def run_both_run_both():
    c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)
    print('starting async process')
    start_time = time.time()
    asyncio.run(run_both())
    print('we done')

    time_split = time.time() - start_time
    print(f'Async Total scraping time: %.2f seconds.' % time_split)

    print('starting sync process')
    run_both_sync()

    time_difference = time.time() - time_split - start_time
    print(f'Total scraping time: %.2f seconds.' % time_difference)
    print(c[1] + f"---> Finished: Time difference = {time_difference - time_split}" + c[0])

run_both_run_both()



