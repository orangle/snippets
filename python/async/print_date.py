# coding:utf-8
"""
两个任务交替进行
"""
import asyncio
from datetime import datetime


async def print_date(loop, num):
    end_time = loop.time() + 10.0
    while True:
        print(datetime.now(), num)
        if (loop.time() + 2.0) >= end_time:
            break 
        await asyncio.sleep(2)
    loop.stop()

loop = asyncio.get_event_loop()
asyncio.ensure_future(print_date(loop, 1))
asyncio.sleep(1)
asyncio.ensure_future(print_date(loop, 2))
loop.run_forever()