import pytest
import asyncio as io


async def gen(iterations):
    for _ in range(iterations):
        await io.sleep(0.1)
        yield 1


@pytest.mark.asyncio
async def test_gen():
    i = 5
    result = [x async for x in gen(5)]
    assert i == len(result)
