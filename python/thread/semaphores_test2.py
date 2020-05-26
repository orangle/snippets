# coding:utf-8
import time
import random
import queue
import threading

orders = queue.Queue()
has_order = threading.Semaphore(value=0)  # ADDED THIS


def serving_line_or_consumer():
    while has_order.acquire():  # ADDED THIS: Acquire a Semaphore, or sleep until the counter of semaphore is larger than zero
        new_order = orders.get()
        print(new_order)
        # prepare meals from `new_order`, assuming GIL is released while preparing meals
        orders.task_done()


def order_line_or_producer():
    # Each staff in the serving line produces 200 orders
    for i in range(200):
        if i%10 == 0:
            time.sleep(3)
        orders.put("Order {}".format(i))
        has_order.release() # ADDED THIS: Release the Semaphore, increment the internal counter by 1


# Let's put 4 staff into the order line
order_line = [threading.Thread(target=order_line_or_producer) for _ in range(2)]

# Let's assign 6 staff into the serving line
serving_line = [threading.Thread(target=serving_line_or_consumer) for _ in range(1)]

# Put all staff to work
[t.start() for t in order_line]
[t.start() for t in serving_line]


# "join" the order, block until all orders are cleared
orders.join()

# "join" the threads, ending all threads
[t.join() for t in order_line]
[t.join() for t in serving_line]