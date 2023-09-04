import paho.mqtt.client as mqttclient
import multiprocessing
import random
import time

# Just for test


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print('Failed to connect, return code %d', rc)


def publish_env():
    broker = 'broker.emqx.io'
    port = 1883
    topic = '/aiot/env'
    client_id = f'python-mqtt-{random.randint(0,100)}'
    username = 'itsmytest'
    password = '112233'
    client = mqttclient.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port, 60)
    client.loop_start()
    msg_number = 1
    while True:
        time.sleep(1)
        msg = f'[{msg_number},{random.uniform(15,35)},{random.uniform(20,100)}]'
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print("Send " + msg + " to " + topic)
        else:
            print("Failed to send message")
        msg_number += 1


def publish_pos():
    broker = 'broker.emqx.io'
    port = 1883
    topic = '/aiot/pos'
    client_id = f'python-mqtt-{random.randint(0,100)}'
    username = 'itsmytest'
    password = '112233'
    client = mqttclient.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port, 60)
    client.loop_start()
    msg_number = 1
    while True:
        time.sleep(1)
        test = random.randint(1,10)
        if(test == 10):
            result = 0
        else:
            result = 1
        msg = f'[{msg_number},{result}]'
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print("Send " + msg + " to " + topic)
        else:
            print("Failed to send message")
        msg_number += 1


if __name__ == '__main__':
    env_publish_process = multiprocessing.Process(target=publish_env)
    pos_publish_process = multiprocessing.Process(target=publish_pos)
    env_publish_process.start()
    pos_publish_process.start()
