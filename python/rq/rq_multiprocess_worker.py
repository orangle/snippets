# coding:utf-8
"""rq 多进程worker的启动脚本"""

import os
import sys
import redis
import argparse
import multiprocessing
from rq import Worker, Queue, Connection
from core.config import config


redis_url = os.getenv('REDISTOGO_URL', 'redis://{}:{}'.format(
    config.get("redis", "host"), config.get("redis", "port")))
conn = redis.from_url(redis_url)


def worker(listen):
    with Connection(conn):
        w = Worker(map(Queue, listen))
        w.work()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="-q xxxx -n 8")
    parser.add_argument("-q", "--queue", dest="queue", required=True,
                        help="worker queue name")
    parser.add_argument("-n", "--num", dest="num", default=1,
                        help="worker number")
    args = parser.parse_args()
    names = [args.queue]
    num = int(args.num)

    for i in range(num):
        multiprocessing.Process(target=worker, args=(names,)).start()

