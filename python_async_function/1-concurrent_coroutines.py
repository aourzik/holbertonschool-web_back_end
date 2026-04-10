#!/usr/bin/env python3
"""async routine wait_n."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """Spawn wait_random n times and return sorted list of delays."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    results = []
    for task in asyncio.as_completed(tasks):
        results.append(await task)

    return results
