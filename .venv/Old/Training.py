import asyncio
from typing import Dict

async def fetch_data() -> Dict: 
    print("Starting fetching data...")
    await asyncio.sleep(2)
    print("Done fetching")
    return {'data': 1}

async def print_data() -> int:
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_data())
    value = await task1
    print(value)
    await task2

asyncio.run(main())

import datetime

async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

asyncio.run(display_date())