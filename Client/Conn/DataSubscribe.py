import paho.mqtt.client as mqttclient
import multiprocessing
import random
import pymysql

# MQTT Connection
def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print("Connected to MQTT Broker!")
	else:
		print('Failed to connect, return code %d', rc)
		
# Database operation
connection = pymysql.connect(host='localhost', user='root', passwd='qwer@123', db='AIoT', charset='utf8')

def env_db_operation(data):
	list = data.strip('[]').split(',')
	cursor = connection.cursor()
	sqlstmt = "INSERT INTO Environment VALUES(%d,%.2f,%.1f,now())"%(int(list[0]),float(list[1]),float(list[2]))
	print("SQL statement: " + sqlstmt)
	cursor.execute(sqlstmt)
	connection.commit()

def pos_db_operation(data):
	list = data.strip('[]').split(',')
	cursor = connection.cursor()
	sqlstmt = "INSERT INTO Posture VALUES(%d,%d,now())"%(int(list[0]),int(list[1]))
	print("SQL statement: " + sqlstmt)
	cursor.execute(sqlstmt)
	connection.commit()
	
# Receive Message
def on_message_env(client, userdata, msg):
	env_db_operation(msg.payload.decode())
	print("Received " + msg.payload.decode() + " from topic " + msg.topic)
	
def on_message_pos(client, userdata, msg):
	pos_db_operation(msg.payload.decode())
	print("Received " + msg.payload.decode() + " from topic " + msg.topic)
	
# Subscribe from publisher
def subscribe_env():
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
	client.subscribe(topic)
	client.on_message = on_message_env
	client.loop_forever()
	
def subscribe_pos():
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
	client.subscribe(topic)
	client.on_message = on_message_pos
	client.loop_forever()
	
if __name__ == '__main__':
	print("Database connection success!")
	env_subscribe_process = multiprocessing.Process(target=subscribe_env)
	pos_subscribe_process = multiprocessing.Process(target=subscribe_pos)
	env_subscribe_process.start()
	pos_subscribe_process.start()