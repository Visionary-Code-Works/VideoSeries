"""asyncio_basics.py
_summary_

_extended_summary_

- `fetch_data` and `process_data` are `async` functions (coroutines) that simulate fetching and processing data, respectively. They use `await asyncio.sleep()` to mimic I/O-bound operations with delays.
- The `main` coroutine schedules `fetch_data` and `process_data` as tasks to run concurrently and waits for their completion.
- `asyncio.run(main())` is used to execute the main coroutine, which in turn runs the other asynchronous tasks.
"""

import asyncio

async def fetch_data():
    """ Simulate a task to fetch data with a delay """
    print("Start fetching data...")
    await asyncio.sleep(2)  # Simulates a delay (e.g., network delay)
    print("Data fetched")

async def process_data():
    """ Simulate a task to process data with a delay """
    print("Start processing data...")
    await asyncio.sleep(1)  # Simulates processing time
    print("Data processed")

async def main():
    """ Main coroutine that runs other tasks """
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(process_data())

    # Wait until both tasks are completed
    await task1
    await task2

if __name__ == "__main__":
    # Running the main coroutine
    asyncio.run(main())
