<<<<<<< HEAD
#!/usr/bin/python3
'''
  Async Comprehension/Generator
'''
import asyncio

=======
#!/usr/bin/env python3

""" Async  Comprehensions """

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Async  Generator """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
>>>>>>> 874979a65ca0b16375dfee123a4440674df76097
