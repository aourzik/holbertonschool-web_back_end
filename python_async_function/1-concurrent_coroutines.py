#!/usr/bin/env python3
"""async routine called wait_n that takes in 2
int arguments (in this order): n and max_delay"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """Spawn wait_random n times and return sorted list of delays.

    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): maximum delay value

    Returns:
        list: list of delays in ascending order
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)
    return results
