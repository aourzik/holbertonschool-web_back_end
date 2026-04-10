#!/usr/bin/env python3
"""Module that contains an async routine wait_n."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """Spawn wait_random n times and return results in ascending order."""
    tasks = [wait_random(max_delay) for _ in range(n)]

    results = []
    for task in asyncio.as_completed(tasks):
        results.append(await task)

    return results
