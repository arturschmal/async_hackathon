import contextvars
import asyncio


my_name = contextvars.ContextVar('my_name')

async def greet():
    await asyncio.sleep(0)
    print(f'Hello {my_name.get()}')

async def set_name():
    name = 'Artur'
    my_name.set(name)

    tasks = []

    tasks.append(greet())
    my_name.set('Guido')
    tasks.append(greet())

    await asyncio.gather(*tasks)

# async def get_name():
#     name = my_name.get()
#     return name

async def main():
    await set_name()

if __name__ == '__main__':
    asyncio.run(main())
     