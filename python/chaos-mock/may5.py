# coding:utf-8
import asyncio
import logging
import random
import string
import uuid
import functools

import attr

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s, %(message)s",
    datefmt="%H:%M:%S"
)

@attr.s
class PubSubMessage(object):
    instance_name = attr.ib()
    message_id = attr.ib(repr=False)
    hostname = attr.ib(repr=False, init=False)
    restarted = attr.ib(repr=False, default=False)
    saved = attr.ib(repr=False, default=False)
    acked = attr.ib(repr=False, default=False)

    def __attrs_post_init__(self):
        self.hostname = f"{self.instance_name}.example.net"


async def publish(queue):
    choices = string.ascii_lowercase + string.digits
    loop = asyncio.get_event_loop()
    while True:
        host_id = "".join(random.choices(choices, k=4))
        msg_id = str(uuid.uuid4)
        instance_name = f"cattle-{host_id}"

        msg = PubSubMessage(message_id=msg_id, instance_name=instance_name)
        # publish an item
        # await queue.put(msg)
        loop.create_task(queue.put(msg))
        logging.info(f"Published messages {msg}")
        await asyncio.sleep(random.random())


async def consume(queue):
    loop = asyncio.get_event_loop()
    while True:
        # wait for an item from the publisher
        msg = await queue.get()
        # the publisher emits None to indicate that it is done
        if msg is None:
            break
        # fanned out 扇出模拟, 得到结果
        await handle_message(msg)


async def handle_message(msg):
    # g_future = asyncio.gather(save(msg), restart_host(msg))
    # callback = functools.partial(cleanup, msg)
    # g_future.add_done_callback(callback)
    # await g_future

    await asyncio.gather(save(msg), restart_host(msg))
    await cleanup(msg)

# 被阻塞
# def cleanup(msg, fut):
#     msg.acked = True
#     logging.info(f"Done. Acke {msg}")

# 非阻塞写法
async def cleanup(msg):
    await asyncio.sleep(random.random())
    msg.acked = True
    logging.info(f"Done acked {msg}")


async def restart_host(msg):
    await asyncio.sleep(random.random())
    msg.restarted = True
    logging.info(f"Restarted {msg.hostname}")

async def save(msg):
    await asyncio.sleep(random.random())
    msg.saved = True
    logging.info(f"Save {msg} into databse")


def main():
    queue = asyncio.Queue()
    loop = asyncio.get_event_loop()

    try:
        loop.create_task(publish(queue))
        loop.create_task(consume(queue))
        loop.run_forever()
    except KeyboardInterrupt:
        logging.info("Process interrupted")
    finally:
        loop.close()
        logging.info("Successfully shutdown the Mayhem service.")

if __name__ == "__main__":
    main()