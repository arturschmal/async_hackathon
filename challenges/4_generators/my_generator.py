import asyncio

async def generator():
    for i in range(10):
        await asyncio.sleep(1)
        yield i


async def run():
    async for i in generator():
        print(i)

def main():
    asyncio.run(run())

if __name__ == "__main__":
    main()