# coding:utf-8
import time
import random

def test_mq(name="hi"):
    print 'mq...'
    for i in range(10):
        print i, name, random.randint(0, 100)
        time.sleep(1)
