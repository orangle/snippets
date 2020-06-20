#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 一个进程并且获取结果, 不要阻塞主流程
# python3.5

import multiprocessing
import time


def worker(x):
    time.sleep(1)
    return x


if __name__ == '__main__':
    pool = multiprocessing.Pool(1)
    print(pool.map(worker, range(3)))
    for x in range(16):
        time.sleep(0.5)
        print(".... {}".format(x))
