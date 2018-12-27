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

r = redis.Redis()
queue_pop = r.register_script(SCRIPT_POP)

if __name__ == "__main__":
    mq_key = "ct:kafka:mq"
    count = 10
    for i in range(count):
        for i in range(count):
            r.zadd(mq_key, "Test_key_{}".format(i), time.time())

    for i in range(count + 10):
        print queue_pop(keys=[mq_key])