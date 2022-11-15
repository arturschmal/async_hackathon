# Async generators

## History PEP 255
Regular generators enabled an elegant way of writing complex data producers and have them behave like an iterator.
However, currently there is no equivalent concept for the asynchronous iteration protocol (async for). This makes writing asynchronous data producers unnecessarily complex, as one must define a class that implements **aiter** and **anext** to be able to use it in an async for statement.

## Current async generator support
`async for` supports iterables of awaitables to be consumbed one-by-one (not concurrently). An async iterator protocol is supported by `__aiter__` and `__anext__` methods or more straight forward a `yield` within a `async def` function. `yield` can also be used within the `__aiter__` method to return an asynchronous iterator. The generator object can optionally have a `__anext__` method that returns the next awaitable and it should call a `StopAsyncIteration` error when depleted. Read more about in the Python datamodel reference.


### Challenge 1
Write an asynchronous iterator using `await` and `yield` and consume it using `async for`. Verify that awaitables are awaited in order and not concurrently.

### Challenge 2
Write two asynchronous iterators, one consuming the other. The first one generates 10 random integers x between 0 and 3 after x seconds of sleep. The second sums the incoming numbers in an internal state and yields the intermediate results.

### Challenge 3
Write two asynchronous iterators that return random integers x between 0 and 10 after a random sleep of max 1 second. 

1. Consume both at the same time with `asyncio.gather` and verify that they are consumed concurrently.
1. Write a third generator that consumes the two asynchronous generators and yields their sum of at each step

## Error handling
In the standard iterator protocol an exception is raised when the iterator is depleted. This holds for the asynchronous iterator with the `StopAsyncIteration` exception.
But what about our exceptions. Where should raise and catch exceptions and how does it relate to the `await` keyword?

### Challenge 4
Write a generator function with `yield` that raises StopAsyncIteration when depleted. Write a `while` loop that awaits the result of the Python 3.10 `anext` and catch the exception to print a final logging line.

### Challenge 5
Introduce a custom error in your generator and consume it asyncio.gather. What line of code needs to be within the `try - except` block for the exception to be catched?


## references

1. https://peps.python.org/pep-0525/
1. https://docs.python.org/3/reference/datamodel.html#asynchronous-iterators
1. https://peps.python.org/pep-0492/#why-aiter-does-not-return-an-awaitable
1. 