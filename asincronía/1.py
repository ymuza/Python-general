"""Minimal asyncio example: a coroutine that awaits a non-blocking sleep."""

import asyncio


async def main():
    print('Hello ...')
    await asyncio.sleep(0.5)
    print('... World!')

asyncio.run(main())
