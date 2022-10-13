# Futures

Future objects are used to bridge low-level callback-based code with high-level async/await code.

The future object is a passable object on which a result can be set by a coroutine. The future object itself is awaitable, which can be very convenient. Especially when interfacing with non async callback based code, although the value of a future can only be set once.

## example
This example creates a Future object, creates and schedules an asynchronous Task to set result for the Future, and waits until the Future has a result:

```
async def set_after(fut, delay, value):
    # Sleep for *delay* seconds.
    await asyncio.sleep(delay)

    # Set *value* as a result of *fut* Future.
    fut.set_result(value)

async def main():
    # Get the current event loop.
    loop = asyncio.get_running_loop()

    # Create a new Future object.
    fut = loop.create_future()

    # create an asynchronous task
    loop.create_task(
        set_after(fut, 1, '... world'))

    print('hello ...')

    # Wait until *fut* has a result (1 second) and print it.
    print(await fut)

asyncio.run(main())
```

## Challenge

1. create a future called `schrodingers_cat`
2. define a coroutine called `schrodingers_box`
3. wait a quantum uncertain amount of time before throwing a dice and assigning either "alive" or "dead" to the value of `schrodingers_cat`
4. await the outcome of your experiment and print the result

## references

1. https://docs.python.org/3/library/asyncio-future.html
