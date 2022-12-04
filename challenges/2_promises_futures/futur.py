import asyncio
import random
import time


async def schrodingers_box(fut, delay):
    # Sleep for *delay* seconds.
    cat_status = ['Alive!', 'Dead!']

    await asyncio.sleep(delay)

    # Set *value* as a result of *fut* Future.
    fut.set_result(random.choice(cat_status))

async def main():

    # Get the current event loop.
    loop = asyncio.get_running_loop()

    # Create a new Future object.
    cats = [loop.create_future() for _ in range(100000)]

    # create an asynchronous task
    tasks = [
        loop.create_task(schrodingers_box(cat, 1)) for cat in cats]


    # Wait until *fut* has a result (1 second) and print it.
    await asyncio.gather(*tasks)
    for index, cat in enumerate(cats):
        print(index, cat.result())

start_time = time.time()
asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
