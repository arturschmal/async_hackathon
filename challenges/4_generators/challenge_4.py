import asyncio as io


async def error_gen():
    for x in range(3):
        yield x
    raise StopAsyncIteration


async def main():
    gen = error_gen()
    while True:
        try:
            x = await gen.__anext__()
            print(f"value consumed: {x}")
        except RuntimeError:
            print("iteration stopped")
            return


if __name__ == "__main__":
    io.run(main())
