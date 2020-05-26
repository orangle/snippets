# coding:utf-8
# The barrier sets up a count of threads that will wait together until that count is reached

import time
import random
import threading

def f(b):
    time.sleep(random.randint(2, 10))
    print("{} woke at: {}".format(threading.current_thread().getName(), time.ctime()))
    b.wait()
    print("{} passed the barrier at: {}".format(threading.current_thread().getName(), time.ctime()))

barrier = threading.Barrier(3)
for i in range(3):
    t = threading.Thread(target=f, args=(barrier,))
    t.start()

"""
$ python barrier_test.py 
Thread-2 woke at: Sun Feb  9 17:25:31 2020
Thread-3 woke at: Sun Feb  9 17:25:33 2020
Thread-1 woke at: Sun Feb  9 17:25:34 2020
Thread-1 passed the barrier at: Sun Feb  9 17:25:34 2020
Thread-2 passed the barrier at: Sun Feb  9 17:25:34 2020
Thread-3 passed the barrier at: Sun Feb  9 17:25:34 2020
"""