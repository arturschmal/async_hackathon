import asyncio
from random import randint

async def generator():
    for i in range(10):
        await asyncio.sleep(randint(1,3))
        i = randint(0,3)
        yield i

async def run():
    async for i in generator():
        print(i)

async def sum():
    async for i in generator():
        print(i + i)
        

def main():
    asyncio.run(sum())

if __name__ == "__main__":
    main()