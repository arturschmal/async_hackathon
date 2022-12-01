import asyncio as io
import random


# challenge 2
async def generate_numbers_and_sleep():
    for _ in range(10):
        x = random.randint(0, 3)
        await io.sleep(x)
        yield x


async def aggregator():
    aggregate = 0
    async for x in generate_numbers_and_sleep():
        aggregate += x
        yield aggregate


async def main():
    async for aggregate in aggregator():
        print(f"current aggregate: {aggregate}")


if __name__ == "__main__":
    io.run(main())


# alternate solution
# class One:
#     def __init__(self) -> None:
#         self.counter = 0

#     def __aiter__(self):
#         return self
    
#     async def __anext__(self):
#         self.counter += 1
#         if self.counter >= 10:
#             raise StopAsyncIteration
#         return self.counter

# class Two:
#     def __init__(self, gen) -> None:
#         self.aggregate = 0
#         self.gen = gen

#     def __aiter__(self):
#         return self
    
#     async def __anext__(self):
#         x = await self.gen.__anext__()
#         self.aggregate += x
#         return self.aggregate


# async def temp():
#     one = One()
#     two = Two(one)
#     async for x in two:
#         print(f"aggregate: {x}")

