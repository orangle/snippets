import redis
import time

SCRIPT_POP = '''
local result = redis.call('ZRANGE', KEYS[1], 0, 0)
local element = result[1]
if element then
    redis.call('ZREM', KEYS[1], element)
    return element
else
    return nil
end
'''

class UniqueQueue(object):

    def __init__(self, key, r_host="127.0.0.1", r_port=6379, r_db=0):
        self.mq_key = key
        self.conn = redis.StrictRedis(r_host, r_port, db=r_db)
        self.queue_pop = self.conn.register_script(SCRIPT_POP)

    def pop(self):
        return self.queue_pop(keys=[self.mq_key])

    def push(self, task):
        return self.conn.zadd(self.mq_key, time.time(), task)
    

if __name__ == "__main__":
    q = UniqueQueue("zset:mq:test")
    count = 10
    for i in range(count):
        for i in range(count):
            q.push("Test_key_{}".format(i))

    for i in range(count + 10):
        print q.pop()