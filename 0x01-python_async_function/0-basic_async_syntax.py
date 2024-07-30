#!/usr/bin/env python3
'''
    Async python- Basic
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        calculate delay: random value between 0 and max_delay
        return delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
