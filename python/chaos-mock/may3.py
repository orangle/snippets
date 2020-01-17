# coding:utf-8
import asyncio
import logging
import random
import string
import uuid

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

    def __attrs_post_init__(self):
        self.hostname = f"{self.instance_name}.example.net"


async def publish(queue, publish_id):
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
        logging.info(f"[{publish_id}] Published messages {msg}")
        await asyncio.sleep(random.randint(0, 5))


async def consume(queue):
    while True:
        # wait for an item from the publisher
        msg = await queue.get()

        # the publisher emits None to indicate that it is done
        if msg is None:
            break

        # process the msg
        logging.info(f"Consumed {msg}")
        # simulate i/o operation using sleep
        await asyncio.sleep(random.random())


def main():
    """多个生产者"""
    queue = asyncio.Queue()
    loop = asyncio.get_event_loop()
    coros = [publish(queue, i) for i in range(1, 4)]

    try:
        [loop.create_task(coro) for coro in coros]
        loop.create_task(consume(queue))
        loop.run_forever()
    except KeyboardInterrupt:
        logging.info("Process interrupted")
    finally:
        loop.close()
        logging.info("Successfully shutdown the Mayhem service.")

if __name__ == "__main__":
    main()