# coding:utf-8
import asyncio
from concurrent.futures import ProcessPoolExecutor

def say_hello(hello):
    i = 0
    while True:
        if i % 10000000 == 0:
            print("...{} {}".format(hello, i))
        i += 1

if __name__ == "__main__":
    executor = ProcessPoolExecutor(2)
    loop = asyncio.get_event_loop()
    boo = asyncio.ensure_future(loop.run_in_executor(executor, say_hello, 'h1'))
    boo = asyncio.ensure_future(loop.run_in_executor(executor, say_hello, 'h2'))
    loop.run_forever()
