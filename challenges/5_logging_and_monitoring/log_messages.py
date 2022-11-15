import asyncio
import datetime


# implement an async "log" function that passes send_message to asyncio.ensure_future


async def send_message(message):
    await asyncio.sleep(1)
    print(message)


def send_some_messages():
    for message in ["first", "second", "third", "etc"]:
        print(f"log {datetime.datetime.now()} : {message}")
        log(message)
