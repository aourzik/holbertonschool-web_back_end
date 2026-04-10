#!/usr/bin/env python3
"""Module to measure the runtime of wait_n."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n(n, max_delay).

    Args:
        n: number of coroutines to spawn
        max_delay: maximum delay in seconds

    Returns:
        total_time / n as a float
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start

    return total_time / n
