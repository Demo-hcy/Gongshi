# -*- coding:utf-8 -*-
# @Time      :2020/12/09

import time
import json
from pprint import pprint

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))


def on_message(client, userdata,msg):
    print(msg.topic + " " + str(msg.payload))
    msg_data = msg.payload
    msg=json.loads(msg_data)
    Time = time.strftime("%Y-%m-%d %H:%M:%S")
    msg.update({"time": Time})

    # timestamp = ((msg['timestamp'])+ 8 * 60 * 60) / 1000
    # Timestamp = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(timestamp))
    # # # msg.update({"timestamp":Timestamp })
    # pprint (Timestamp)
    pprint(msg)
    print("--"*50)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username="mosquitto", password="tN9NQe#fPh")
client.connect('192.168.49.68', 1883, 60) # 600为keepalive的时间间隔
client.subscribe('#', qos=0)
client.loop_forever() # 保持连接


