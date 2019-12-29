# coding:utf-8
import redis 
import time

rconn = redis.StrictRedis()

def mock_status():
    """mock some datas instert into redis as test case
    """
    start = int(time.time())
    for i in range(100000):
        value = start + i
        rconn.hset("test:hash", value, value)
        rconn.sadd("test:set", value, value)
        rconn.zadd("test:zset", value, value)
        rconn.lpush("test:list", value, value)


def del_big_hash(key_name):
    cursor = '0'
    while cursor != 0:
        cursor, datas = rconn.hscan(key_name, cursor=cursor, count=200)
        for item in datas.items():
            rconn.hdel(key_name, item[0])
    

def del_big_set(key_name):
    cursor = '0'
    while cursor != 0:
        cursor, datas = rconn.sscan(key_name, cursor=cursor, count=200)
        for item in datas:
            if int(item)%2 == 0:
                rconn.srem(key_name, item)


def del_big_zset(key_name):
    cursor = '0'
    while cursor != 0:
        cursor, datas = rconn.zscan(key_name, cursor=cursor, count=200)
        for item in datas:
            rconn.zrem(key_name, item[0])


def del_big_list(key_name):
    llen = rconn.llen(key_name)
    counter = 0
    left = 100
    while counter < llen:
        rconn.ltrim(key_name, 100, llen)
        counter += left
    rconn.delete(key_name)


if __name__ == "__main__":
    # mock_status()
    # del_big_hash("test:hash")
    del_big_set("test:set")
    # del_big_zset("test:zset")
    # del_big_list("test:list")