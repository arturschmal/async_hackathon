import asyncio as io
import random
import time


async def process():
    rand_num = random.randint(0, 4)
    await io.sleep(rand_num)
    return rand_num


async def main():
    # start times
    start_time = time.time()

    # create and execute tasks
    tasks = [io.create_task(process()) for _ in range(10)]
    results = await io.gather(*tasks)

    # print results
    for result in results:
        print(f"coroutine worked for {result} seconds")

    # print total execution time
    print(f"total execution time: {time.time() - start_time}")


if __name__ == "__main__":
    io.run(main())
