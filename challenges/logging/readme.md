# Logging in async apps

Standard logging with the logger module is synchronous. We can use the QueueHandler to push our log events into a queue and run a QueueListener to process them offline. It was designed for multiprocessing, but is perfectly usable in the async context.

## references

1. https://docs.python.org/3/library/logging.handlers.html#queuehandler
1. https://docs.python.org/3/library/logging.handlers.html#queuelistener
1. https://www.zopatista.com/python/2019/05/11/asyncio-logging/
