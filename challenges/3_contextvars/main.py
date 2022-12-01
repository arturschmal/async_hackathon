import asyncio as io
from contextvars import ContextVar

name_var = ContextVar[str]("simple_context")


async def greeting():
    await io.sleep(1)
    print(f"\n\t- hello there!\n\t- general {name_var.get()}...\n")


async def main():
    while True:
        name_var.set(input("what is you name?\n"))
        await greeting()


if __name__ == "__main__":
    io.run(main())
