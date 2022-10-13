# Debugging and logging async code

# Monitoring for debugging
With aiomonitor we can listen to our running async code and get an interactive console to inspect our event loop and tasks.

## Debugging
A debugger needs event loop support to allow it to introspect or evaluate async results.

## Logging in async apps

Standard logging with the logger module is synchronous. We can use the QueueHandler to push our log events into a queue and run a QueueListener to process them offline. It was designed for multiprocessing, but is perfectly usable in the async context.

## references

1. https://docs.python.org/3/library/logging.handlers.html#queuehandler
1. https://docs.python.org/3/library/logging.handlers.html#queuelistener
1. https://www.zopatista.com/python/2019/05/11/asyncio-logging/
1. https://codebeez.nl/blogs/europython-2022-summaries-of-selected-talks/