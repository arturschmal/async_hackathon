import asyncio as io


# challenge 1
async def async_gen():
    for x in range(10):
        yield x


async def main():
    async for x in async_gen():
        print(x)


if __name__ == "__main__":
    io.run(main())
