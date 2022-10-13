# Async basics to get started

## event loop tasks (coroutines)

asyncio is a library to write concurrent code using the async/await syntax.
asyncio is often a perfect fit for IO-bound and high-level structured network code.

asyncio provides a set of high-level APIs to:

1. run Python coroutines concurrently and have full control over their execution
1. perform network IO and IPC
1. control subprocesses
1. distribute tasks via queues
1. synchronize concurrent code

## Hello world

```
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())
```
This "Hello World" contains the concepts to get started with asyncio in Python, which we will explain below.

Notice that in the "Hello World" example a synchronous functions `print` is called within an asynchronous function. Calling synchronous functions is not good practice as it blocks the CPU and we might lose the benefit of concurrently executing Python code.
In our challenge about logging we will see ways of logging asynchronously.

### async/await

The `async` and `await` keywords are two sides of the same coin. A concurrent function (coroutine) defined with `async def` needs to be awaited with `await` when called as the result will not be available directly.

#### Awaitables
We say that an object is an awaitable object if it can be used in an await expression. Many asyncio APIs are designed to accept awaitables.
There are three main types of awaitable objects: coroutines, Tasks, and Futures.

### event loop
In most cases we can speak of 1 event loop in our Python software. One event loop that coordinates the tasks that are based on a set of coroutines. When we `await` a coroutine we define an execution context that the event loop can pass control to accompanied with the asynchronous result for further processing.

```
 asyncio.run(coroutine)
```
This function always creates a new event loop and closes it at the end. It should be used as a main entry point for asyncio programs, and should ideally only be called once. This function cannot be called when another asyncio event loop is running in the same thread.

### tasks
Tasks are used to schedule coroutines concurrently. When a coroutine is wrapped into a Task with functions like asyncio.create_task() the coroutine is automatically scheduled to run soon.

```
import asyncio

async def nested():
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task

asyncio.run(main())
```
## Challenge
Alter the above task code to start multiple tasks concurrently and collect the tasks in a list.
Each task should wait a random amount of seconds and then return the amount of seconds that they slept.
Get the results of all tasks with [`gather`](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather) and print them.


## references

1. https://docs.python.org/3/library/asyncio.html
1. https://docs.python.org/3/library/asyncio-task.html#coroutines-and-tasks