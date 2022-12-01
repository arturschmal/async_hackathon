import asyncio as io
import datetime


# implement an async "log" function that passes send_message to asyncio.ensure_future
def log(message):
    task = io.create_task(send_message(message))
    io.ensure_future(task)


async def send_message(message):
    await io.sleep(1)
    print(message)


async def send_some_messages():
    for message in ["first", "second", "third", "etc"]:
        print(f"log {datetime.datetime.now()} : {message}")
        log(message)

    # sleed for a bit so the background tasks also have time to complete
    await io.sleep(2)


if __name__ == "__main__":
    io.run(send_some_messages())
