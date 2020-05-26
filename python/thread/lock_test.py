# coding:utf-8
from threading import Lock, Thread

lock = Lock()
g = 0

def add_one():
    global g
    lock.acquire()
    g += 1
    lock.release()


def add_two():
    global g
    lock.acquire()
    g += 2
    lock.release()

threads = []
for func in [add_one, add_two]:
    threads.append(Thread(target=func))
    threads[-1].start()

for t in threads:
    t.join()

print(g)