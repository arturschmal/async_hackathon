import asyncio as io
import random


async def schrodingers_box(fut):
    quantum_uncertain_time = random.randint(1, 10)
    await io.sleep(quantum_uncertain_time)
    dead_or_alive = "alive" if quantum_uncertain_time % 2 == 0 else "dead"
    fut.set_result(dead_or_alive)


async def main():
    # create future
    loop = io.get_running_loop()
    fut = loop.create_future()

    # create task
    io.create_task(schrodingers_box(fut))

    # drumroll
    print("you cat is... ")
    print((await fut).upper())


if __name__ == "__main__":
    io.run(main())
