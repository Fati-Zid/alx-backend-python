#!/usr/bin/env python3
'''
    The basics of async
'''

import asyncio
import random
from './0-basic_async_syntax.py' import wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """
    create list of tasks.
    spawn wait random n times with the specified max_delay.
    """
    tasks = [
       asyncio.create_task(wait_random(max_delay))
       for _ in range(n)
    ]
    return [await tasks for task in asyncio.as_completed(tasks)]
