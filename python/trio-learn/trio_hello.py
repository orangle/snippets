import trio

async def async_double(x):
    print(2*x)

trio.run(async_double, 3)