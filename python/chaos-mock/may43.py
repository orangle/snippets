import logging
import queue
import random
import string
import time
import uuid
import asyncio
import concurrent.futures
import signal

import attr

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,%(msecs)d %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)

@attr.s
class PubSubMessage:
    instance_name = attr.ib()
    message_id    = attr.ib(repr=False)
    hostname      = attr.ib(repr=False, init=False)

    def __attrs_post_init__(self):
        self.hostname = f"{self.instance_name}.example.net"


async def publish(executor, queue):
    logging.info("Starting publisher")
    loop = asyncio.get_event_loop()
    # return future.Feture
    futures = [
        loop.run_in_executor(executor, publish_async, queue) for i in range(5)
    ]
    asyncio.ensure_future(asyncio.gather(*futures, return_exceptions=True))


def publish_async(queue):
    choices = string.ascii_lowercase + string.digits

    while True:
        msg_id = str(uuid.uuid4())
        host_id = "".join(random.choices(choices, k=4))
        instance_name = f"cattle-{host_id}"
        msg = PubSubMessage(message_id=msg_id, instance_name=instance_name)
        # publish an item
        queue.put(msg)
        logging.info(f"Published {msg}")
        time.sleep(random.random())


async def consume(executor, queue):
    logging.info("Starting consumer")
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(executor, consume_async, queue) for i in range(5)
    ]
    asyncio.ensure_future(asyncio.gather(*futures, return_exceptions=True))


def consume_async(queue):
    while True:
        # wait for an item from the publisher
        msg = queue.get()
        logging.info(f"Consumed {msg}")
        # simulate i/o operation using sleep
        time.sleep(random.random())


async def shutdown(loop, executor, signal=None):
    """Cleanup tasks tied to the service's shutdown."""
    if signal:
        logging.info(f"Received exit signal {signal.name}...")
    logging.info("Closing database connections")
    logging.info("Nacking outstanding messages")
    loop = asyncio.get_event_loop()
    tasks = [t for t in asyncio.Task.all_tasks() if t is not
             asyncio.Task.current_task()]
    [task.cancel() for task in tasks]

    logging.info(f"Cancelling {len(tasks)} outstanding tasks")
    await asyncio.gather(*tasks, return_exceptions=True)

    logging.info("shutting down executor")
    executor.shutdown(wait=False)
    logging.info(f"Releasing {len(executor._threads)} threads from executor")
    for thread in executor._threads:
        try:
            thread._tstate_lock.release()
        except Exception:
            pass

    logging.info(f"Flushing metrics")
    loop.stop()

def main():
    executor = concurrent.futures.ThreadPoolExecutor()
    loop = asyncio.get_event_loop()
    signals = (signal.SIGHUP, signal.SIGTERM, signal.SIGINT)
    for s in signals:
        loop.add_signal_handler(
            s, lambda s=s: loop.create_task(shutdown(loop, executor, signal=s)))
    q = queue.Queue()

    try:
        loop.create_task(publish(executor, q))
        loop.create_task(consume(executor, q))
        loop.run_forever()
    finally:
        loop.close()
        logging.info("Successfully shutdown the Mayhem service.")

if __name__ == "__main__":
    main()