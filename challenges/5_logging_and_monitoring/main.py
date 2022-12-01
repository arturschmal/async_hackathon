import asyncio as io
import aiomonitor
from aiohttp import web


def log(message, loop):
    task = io.create_task(send_message(message))
    io.ensure_future(task, loop=loop)


async def send_message(message):
    await io.sleep(100)
    print(message)


async def simple(request):
    loop = request.app.loop

    log("hello there", loop=loop)
    await io.sleep(10, loop=loop)
    return web.Response(text="Simple answer")


loop = io.get_event_loop()
host, port = "0.0.0.0", 8080

locals_ = {"port": port, "host": host}

# init monitor just before run_app
with aiomonitor.start_monitor(loop=loop, locals=locals_):
    loop = io.get_event_loop()

    # create application and register route
    app = web.Application()
    app.router.add_get("/simple", simple)

    # run application with built-in aiohttp run_app function
    web.run_app(app, port=port, host=host, loop=loop)
