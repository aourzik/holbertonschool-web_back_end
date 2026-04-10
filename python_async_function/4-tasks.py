#!/usr/bin/env python3
"""Module that contains task_wait_n."""

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """Spawn task_wait_random n times and return sorted delays."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    results = []
    for task in asyncio.as_completed(tasks):
        results.append(await task)

    return results
