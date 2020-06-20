import asyncio
import time 


async def count():
    print(1)
    await asyncio.sleep(1)
    print(2)
    time.sleep(1)
    print(3)


async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    t = time.perf_counter() - s 
    print("cost time {}".format(t))