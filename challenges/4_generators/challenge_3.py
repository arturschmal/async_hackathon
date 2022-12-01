import asyncio as io
import random


# challenge 3
async def generate_numbers_and_sleep(name):
    for _ in range(10):
        x = random.randint(0, 10)
        await io.sleep(random.random())
        print(f"{name} yields {x}")
        yield x


async def generator_consumer(gen):
    aggregate = 0
    async for x in gen:
        aggregate += x
    return aggregate


async def anext(gen):
    try:
        return await gen.__anext__()
    except StopAsyncIteration:
        raise


async def generator_consumer_sum(gen_1, gen_2):
    while True:
        try:
            result = sum(await io.gather(anext(gen_1), anext(gen_2)))
            print(f"intermediate aggregate: {result}")
            yield result
        except StopAsyncIteration:
            return


async def main():
    # subchallenge 1
    print("challenge 1")
    result = await io.gather(
        generator_consumer(generate_numbers_and_sleep("kenobi")),
        generator_consumer(generate_numbers_and_sleep("grievous")),
    )
    print(f"subchallenge 1 result: {result}")

    # subchallenge 2
    print("\n\nchallenge 2")
    step_sums = [x async for x in generator_consumer_sum(
        generate_numbers_and_sleep("kenobi"),
        generate_numbers_and_sleep("grievous")
    )]
    print(f"subchallenge 2 result: {step_sums}")


if __name__ == "__main__":
    io.run(main())
