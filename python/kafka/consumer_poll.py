# coding:utf-8
import json

import six
from kafka import KafkaConsumer


consumer = KafkaConsumer("ct_access_log", 
                        bootstrap_servers="192.168.1.210:9092",
                        group_id="elmeast")

for message in consumer:
    # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
    #                                       message.offset, message.key,
    #                                       message.value))
    msg_dict = json.loads(message.value)   
    print msg_dict.get("url")
    

