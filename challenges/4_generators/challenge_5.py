import asyncio as io


class CustomException(Exception):
    pass


async def custom_error_gen():
    for x in range(10):
        if x == 7:
            raise CustomException
        yield x


async def consumer(gen):
    return [x async for x in gen]


async def main():
    try:
        await io.gather(consumer(custom_error_gen()))
    except CustomException:
        print("compiler: CUSTOM EXCEPTION RAISED")
        print("developer: oh no... what am I gonna do...")


if __name__ == "__main__":
    io.run(main())
