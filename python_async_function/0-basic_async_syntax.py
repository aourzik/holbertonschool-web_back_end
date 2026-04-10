#!/usr/bin/env python3
"""This module contains a floor function that
takes a float n as argument and returns the
floor of the float."""
import math
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """This function takes an integer argument max_delay
    and returns a random delay between 0 and
    max_delay (included) in seconds."""
    delay = max_delay * math.random()
    await asyncio.sleep(delay)
    return delay
