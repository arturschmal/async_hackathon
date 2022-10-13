# Async generators

Regular generators (introduced in PEP 255) enabled an elegant way of writing complex data producers and have them behave like an iterator.

However, currently there is no equivalent concept for the asynchronous iteration protocol (async for). This makes writing asynchronous data producers unnecessarily complex, as one must define a class that implements **aiter** and **anext** to be able to use it in an async for statement.

## references

1. https://peps.python.org/pep-0525/
