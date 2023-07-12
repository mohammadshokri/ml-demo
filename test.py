
import json
from pykafka import KafkaClient
import threading
from kafka import KafkaConsumer
import sys
from pymongo import MongoClient


def getData():
	conn = MongoClient(host='10.39.15.41',port=1522)
	db = conn.galaxy
    collection = db.event
    bootstrap_servers = ['10.39.15.41:9092']
    topicName = 'EventTopic'

    consumer = KafkaConsumer (topicName,bootstrap_servers = bootstrap_servers)

    for msg in consumer:
        # print("Topic Name=%s,
        # Message=%s"%(msg.topic,msg.value))
        print (msg.value.decode('utf-8'))
        try:
            rec_id1 = collection.insert_one(msg.value.decode('utf-8'))
        except:
			print("Failed table {} creation!".format(table))
			logging.error("Failed creation of table+{}+0+0+0".format(table))
    sys.exit()
getData()
