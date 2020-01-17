import time
import trio

async def broken_double_sleep(x):
    print("going to sleep")
    start_time = time.perf_counter()
    await trio.sleep(2 * x)
    sleep_time = time.perf_counter() - start_time
    print("woke up after {}".format(sleep_time))

trio.run(broken_double_sleep, 3)