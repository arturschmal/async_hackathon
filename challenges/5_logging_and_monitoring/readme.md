# Debugging and logging async code

## Logging in async apps

Standard logging with the logger module is synchronous. We can use various techniques to do none blocking logging.

## Challenge option 1

Open ./logging.py.

1. implement a "log" function that passes send_message to asyncio.ensure_future

## Challenge option 2

Use The QueueHandler to push our log events into a queue and run a QueueListener to process them offline. It was designed for multiprocessing, but is perfectly usable in the async context. See the Zopatista blog in the references.

# Monitoring async applications

With aiomonitor we can listen to our running async code and get an interactive console to inspect our event loop and tasks.

# Challenge
Wrap your logging application (make it log forever) with aiomonitor or follow the tutorial on the aiomonitor to wrap a simple http server. Connect with aiomonitor from a separate terminal. Execute aiomonitor commands to do the following.

1. show a table of alive tasks
1. print a stacktrace from the event loop thread
1. open console to get a Python REPL


## references
1. 1. https://docs.python.org/3/library/asyncio-dev.html#asyncio-logger
1. https://www.zopatista.com/python/2019/05/11/asyncio-logging/
1. https://docs.python.org/3/library/logging.handlers.html#queuehandler
1. https://docs.python.org/3/library/logging.handlers.html#queuelistener
1. https://aiomonitor.readthedocs.io/en/latest/
1. https://aiomonitor.readthedocs.io/en/latest/tutorial.html
