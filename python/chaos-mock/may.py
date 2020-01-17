# coding:utf-8
import asyncio
import logging
import random
import string

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


async def publish(queue, n):
    choices = string.ascii_lowercase + string.digits
    for x in range(1, n + 1):
        host_id = "".join(random.choices(choices, k=4))
        instance_name = f"cattle-{host_id}"
        msg = PubSubMessage(message_id=x, instance_name=instance_name)
        # publish an item
        await queue.put(msg)
        asyncio.sleep(0.5)
        logging.info(f"Published {x} of {n} messages")

    # indicate the publisher is done
    await queue.put(None)


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
    queue = asyncio.Queue()
    loop = asyncio.get_event_loop()

    try:
        # 这两个任务依然是阻塞的
        loop.create_task(publish(queue, 5))
        loop.create_task(consume(queue))
        loop.run_forever()
    except KeyboardInterrupt:
        logging.info("Process interrupted")
    finally:
        loop.close()
        logging.info("Successfully shutdown the Mayhem service.")

if __name__ == "__main__":
    main()