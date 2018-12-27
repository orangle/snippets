# coding:utf-8

import redis

SCRIPT_PUSH = '''
local q = KEYS[1]
local q_set = KEYS[1] .. "_set"
local v = redis.call("SADD", q_set, ARGV[1])
if v == 1
then
	return redis.call("RPUSH", q, ARGV[1]) and 1
else
	return 0
end
'''


SCRIPT_POP = '''
local q = KEYS[1]
local q_set = KEYS[1] .. "_set"
local v = redis.call("LPOP", q)
if v then
	redis.call("SREM", q_set, v)
end
return v
'''

r = redis.Redis()
queue_push = r.register_script(SCRIPT_PUSH)
queue_pop = r.register_script(SCRIPT_POP)

if __name__ == "__main__":
    mq_key = "ct:kafka:mq"
    count = 10
    for i in range(count):
        for i in range(count):
            queue_push(keys=[mq_key], args=['Test_key_{}'.format(i)])
     
    for i in range(count + 10):
        print queue_pop(keys=[mq_key])