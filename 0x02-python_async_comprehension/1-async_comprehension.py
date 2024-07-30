<<<<<<< HEAD
#!/usr/bin/python3
=======
#!/usr/bin/env python3

""" Async  Comprehensions """

from asyncio import sleep
from random import uniform
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Async  Comprehensions  """
    a = [i async for i in async_generator()]
    return a
>>>>>>> 874979a65ca0b16375dfee123a4440674df76097
