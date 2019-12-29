import asyncio

async def hello_world():
    print('hello')

loop = asyncio.get_event_loop()
loop.run_until_complete(hello_world())
loop.stop()