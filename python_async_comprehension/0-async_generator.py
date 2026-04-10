#!/usr/bin/env python3
"""Module containing async_generator coroutine."""

import asyncio
import random


async def async_generator(): # type: ignore
    """Asynchronously yield 10 random numbers between 0 and 10.

    Waits 1 second between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
