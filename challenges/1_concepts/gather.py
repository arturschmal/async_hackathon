import asyncio
from random import randint

# async def main():
#     print('Hello ...')
#     await asyncio.sleep(10)
#     print('... World!')

# asyncio.run(main())


async def nested():
    await asyncio.sleep(randint(1,10))
    interval = randint(25,50)
    print(interval)
    return(interval)

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task_1 = asyncio.create_task(nested())
    task_2 = asyncio.create_task(nested())
    task_3 = asyncio.create_task(nested())

    tasks = await asyncio.gather(
        task_1,
        task_2,
        task_3,
    )

    print(tasks)


asyncio.run(main())
