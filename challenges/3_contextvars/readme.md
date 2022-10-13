# Contextvars

Contextvars provide APIs to manage, store, and access context-local state. The ContextVar class is used to declare and work with Context Variables. The copy_context() function and the Context class should be used to manage the current context in asynchronous frameworks.

## example from docs

This example shows tha a context variable set within an asynchronous task are available within that task.

```
import asyncio
import contextvars

client_addr_var = contextvars.ContextVar('client_addr')

def render_goodbye():
    # The address of the currently handled client can be accessed
    # without passing it explicitly to this function.

    client_addr = client_addr_var.get()
    return f'Good bye, client @ {client_addr}\n'.encode()

async def handle_request(reader, writer):
    addr = writer.transport.get_extra_info('socket').getpeername()
    client_addr_var.set(addr)

    # In any code that we call is now possible to get
    # client's address by calling 'client_addr_var.get()'.

    while True:
        line = await reader.readline()
        print(line)
        if not line.strip():
            break
        writer.write(line)

    writer.write(render_goodbye())
    writer.close()

async def main():
    srv = await asyncio.start_server(
        handle_request, '127.0.0.1', 8081)

    async with srv:
        await srv.serve_forever()

asyncio.run(main())
```
## Challenge

1. create a contextvar
2. create two nested coroutines
3. the outer coroutine sets the value of the contextvar
4. the inner coroutine gets the value of the contextvar

## references

1. https://docs.python.org/3/library/contextvars.html#module-contextvars
1. https://docs.python.org/3/library/contextvars.html#asyncio-support
