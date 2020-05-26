# coding:utf-8
import time
import random   
from threading import BoundedSemaphore, Thread

max_items = 1 
container = BoundedSemaphore(max_items)

def producer(nloops):
    for i in range(nloops):
        time.sleep(random.randrange(2,5))
        print(time.ctime(), end=":")
        try:
            container.release()
            print("produced an item")
        except ValueError:
            print("procuder Full, skipping.")

def consumer(nloops):
    for i in range(nloops):
        time.sleep(random.randrange(2, 5))
        print(time.ctime(), end=":")
        if container.acquire(False):
            print("consumer an itme")
        else:
            print("consumer Empty, skipping")

threads = []
nloops = random.randrange(3, 6)
cnloops = random.randrange(nloops, nloops+max_items+2)
print(nloops, cnloops)
threads.append(Thread(target=producer, args=(nloops,)))
threads.append(Thread(target=consumer, args=(cnloops,)))

for t in threads:
    t.start()

for t in threads:
    t.join()
print("All done")
