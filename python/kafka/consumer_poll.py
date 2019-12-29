# coding:utf-8
import json

import six
from kafka import KafkaConsumer
from kafka import KafkaProducer

servers = '192.168.1.210:9092'

def consumer():
    consumer = KafkaConsumer("yudongYun", 
                            bootstrap_servers=servers,
                            group_id="elmeast")

    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                            message.offset, message.key,
                                            message.value))
        # msg_dict = json.loads(message.value)   
        # print msg_dict.get("url")
    

def producer():
    msg = """{"serverIp":"150.138.138.35","timestamp":"1545951636","respondTime":"88","httpCode":"304","eventTime":"07:00:36","clientIp":"111.63.51.81","clientPort":"-","method":"GET","protocol":"http","channel":"pic.nova.net.cn","url":"/uploads/allimg/180903/1435043626-2.jpg","httpVersion":"HTTP/1.1","bodyBytes":"359","destIp":"-","destPort":"-","status":"TCP_MISS","referer":"www.baidu.com","Ua":"spider-ads","fileType":"-","type":"yudongYun"}"""
    producer = KafkaProducer(bootstrap_servers=servers)
    producer.send("yudongYun", msg)
    producer.flush()

producer()
#consumer()