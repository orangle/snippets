import re
import gzip
import time

test_str = "182.91.62.173 - - [20/Nov/2018:20:23:48 +0800] 1 \"GET http://7img1.tianlaikge.com/images/20181112/e4c6f9cf-d829-4965-967d-676571864b87.jpg?imageMogr2/thumbnail/360x HTTP/1.1\" 200 26913 26272 \"-\" \"-\" \"Dalvik/2.1.0 (Linux; U; Android 5.0.1; 8S72 G6 Build/LRX22C)\" \"-\" 177659333 \"HIT\" 211.97.82.35"
regex = r"(?P<client_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<time>\S+) \S+\] (?P<cost>\d+) \"(?P<method>\S+) (?P<url>\S+) (?P<protocol>\S+) (?P<status>\S+) (?P<bytes_sent>\S+) (?P<body_bytes_sent>\S+) \"(?P<referer>\S+)\" \"(?P<cookie>\S+)\" \"(?P<user_agent>.*?)\" \"(?P<x_forworded_for>\S+)\" (?P<conn_id>\S+) \"(?P<is_hit>\S+)\" (?P<server_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
c_regex = re.compile(regex)

def split_parse(line):
    s_space = line.split()
    s_quota = line.split('"') 
    try:
        client_ip = s_space[0]
        time = s_space[3]
        cost = s_space[5]
        method = s_space[6]
        url = s_space[7]
        protocol = s_space[8]
        status = s_space[9]
        byte_send = int(s_space[10])
        body_byte_send = s_space[11]
        server_ip = s_space[-1]
        ishit = s_space[-2]
        referer = s_quota[3]
        user_agent = s_quota[7]
    except Exception as e:
        print "error", line
    
    # print "|".join([client_ip, time, cost, method, url,
    #  protocol, status, str(byte_send), body_byte_send, 
    #  server_ip, ishit, referer, user_agent])
    return byte_send 


def regex_parse(line):
    matches = re.findall(regex, line)
    res = 0
    if len(matches) > 0:
        try:
            res = int(matches[0][7])
        except Exception as e:
            print "error", line
    return res

def regex_compile_parse(line):
    matches = c_regex.findall(line)
    res = 0
    if len(matches) > 0:
        try:
            res = int(matches[0][7])
        except Exception as e:
            print "error", line
    return res


if __name__ == "__main__":
    fname = "/Users/liuzhizhi/udn/testdatas/7img1.tianlaikge.com.gz"
    total = 0
    count = 0
    start = time.time()
    
    with gzip.open(fname) as f:
        for line in f:
            #bytess = regex_parse(line)
            #bytess = regex_compile_parse(line)
            bytess = split_parse(line)
            total += bytess
            count += 1

    cost = time.time() - start
    print "total bytes: {} cost: {} qps: {}".format(total, round(cost, 3), round(count/cost, 3)) 

    




