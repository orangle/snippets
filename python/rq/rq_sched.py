# coding:utf-8
import time
from redis import Redis
from rq import Queue
from rq_scheduler import Scheduler
from datetime import datetime, timedelta

scheduler = Scheduler(connection=Redis(), queue_name='Log') # Get a scheduler for the "default" queue

def hello():
    for i in range(10):
        print time.time(), i

scheduler.enqueue_in(timedelta(minutes=1), hello)