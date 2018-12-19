# coding:utf-8
"""rq 多进程worker的启动脚本"""

import os
import sys
import signal
import redis
import argparse
import multiprocessing
from rq import Worker, Queue, Connection
from core.config import config

pid_list = []

all_sigs = dict((getattr(signal, n), n) \
    for n in dir(signal) if n.startswith('SIG') and '_' not in n )
redis_url = os.getenv('REDISTOGO_URL', 'redis://{}:{}'.format(
    config.get("redis", "host"), config.get("redis", "port")))
conn = redis.from_url(redis_url)


def sigint_handler(signum,frame):
    print signum, "********"
    for i in pid_list:
        os.kill(i, signal.SIGKILL)
    sys.exit()


def print_msg(signum, frame):
    print signum, "***"


def worker(listen):
    with Connection(conn):
        w = Worker(map(Queue, listen))
        w.work()


signal.signal(signal.SIGINT, sigint_handler)

uncatchable = ['SIG_DFL','SIGSTOP','SIGKILL']
for i in [x for x in dir(signal) if x.startswith("SIG")]:
    if i not in uncatchable:
        signum = getattr(signal, i)
        signal.signal(signum, print_msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="-q xxxx -n 8")
    parser.add_argument("-q", "--queue", dest="queue", required=True,
                        help="worker queue name")
    parser.add_argument("-n", "--num", dest="num", default=1,
                        help="worker number")
    args = parser.parse_args()
    names = [args.queue]
    num = int(args.num)

    pool = multiprocessing.Pool(processes=num)
    for i in range(num):
        pool.apply_async(worker, args=(names,))

    for i in multiprocessing.active_children():
        pid_list.append(i.pid)

    pid_list.append(os.getpid())
    pool.close()
    pool.join()
