import asyncio
import aiomonitor
from aiohttp import web
import nest_asyncio

nest_asyncio.apply()

# Simple handler that returns response after 100s
async def simple(request):
    loop = request.app.loop

    print("Start sleeping")
    await asyncio.sleep(1, loop=loop)
    print("Finished sleeping")
    return web.Response(text="Simple answer")


loop = asyncio.get_event_loop()
host, port = "0.0.0.0", 8080

locals_ = {"port": port, "host": host}

# init monitor just before run_app
with aiomonitor.start_monitor(loop=loop, locals=locals_):
    loop = asyncio.get_event_loop()

    # create application and register route
    app = web.Application()
    app.router.add_get("/simple", simple)

    # run application with built-in aiohttp run_app function
    web.run_app(app, port=port, host=host)
