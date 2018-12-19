# python2


启动worker
```
python rq_worker.py -q task -n 10
```

inqueue
```
import redis
from rq import Queue
from rq_job import test_mq

q = Queue(connection=redis.Redis(), name="task")
q.enqueue(test_mq)
```

* rq 直接使用多进程启动的问题是 kill 的时候会导致运行的job失败，使用信号可以 warm shutdown, 但是有个疑问，如果开了10个进程，只有一个在 active 并且还是长时间的任务，这个时候重启是什么效果？

其他9个立刻被kill了，但是这一个long job一直等待他完成，然后才能重新成功，这样的话会造成后续的job堆积。

一次ctrl c会自动优雅退出
```
^C10:02:51 Warm shut down requested
10:02:51 Warm shut down requested
10:02:51 Warm shut down requested
10:02:51 Warm shut down requested
10:02:51 Warm shut down requested
10:02:51 Warm shut down requested
10:02:51 Warm shut down requested
10:02:51 Warm shut down requested
10:02:51 Warm shut down requested
10:02:51 Warm shut down requested
```

二次ctrl c, 就无法退出了

为了不让job堆积，可以在long time job还在shut down的时候，启动新的worker消费后续的job，有点类似nginx的reload，老worker继续退出，新的已经开始工作。
或者不使用信号来优雅退出，直接让任务失败，然后重新加入到queue中。


* rq 当job的逻辑改变了之后，即使不重启worker也会按照新job的逻辑执行，这时候就需要生产者（inqueue)的时候一定要和worker重启的时间一致，或者说不要轻易改变 inqueue 时候的参数。

测试的时候不重启worker，直接修改 rq_job.py, 然后inqueue

* rq_multiprocess_worker.py 和 rq_worker.py 都是优雅退出，有点不符合预期

* `rq_task.ini` 是 http://python-rq.org/patterns/supervisor/ 的配置，warm shutdown 也只有10s的超时时间，10秒之后还是被kill掉 