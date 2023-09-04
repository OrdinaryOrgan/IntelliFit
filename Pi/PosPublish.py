import time
import datetime
from bluetooth import ble
import csv
import numpy as np
import os
from bluezero import microbit
import cv2
from ML import ImageProcesser
import math
import RPi.GPIO as GPIO
from distutils.log import error
import random
import paho.mqtt.client as mqttclient
import mediapipe as mp


mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def draw_landmarks(img, results):
    mp_draw = mp.solutions.drawing_utils
    mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    return img
    
    
#LED_INITIALIZATION

GPIO.setmode(GPIO.BCM)
LEDPin = 23
GPIO.setup(LEDPin,GPIO.OUT)
GPIO.output(LEDPin,GPIO.LOW)


print("Program running... Press CTRL+C to exit")


cap = cv2.VideoCapture(0)
Processor = ImageProcesser()

def addBleUartDevice(address, name):
    bleUartDevice = microbit.Microbit(address)
    bleUartDevice.connect()
    bleUartDevices.append({'name':name, 'Ubitt':bleUartDevice})



#MQTT####
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print('Failed to connect, return code %d', rc)

def publish_pos():
    broker = 'broker.emqx.io'
    port = 1883
    topic = '/aiot/pos'
    client_id = f'python-mqtt-{random.randint(0,100)}'
    username = 'itsmytest'
    password = '112233'
    statelist = [1,1,1]
    client = mqttclient.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port, 60)
    client.loop_start()
    msg_number = 1
    res = 1
    while True:
        time.sleep(0.00001)
        for i in range(3):
            success, img = cap.read()
            cv2.imwrite('/home/pi/Documents/image.jpg',img)
            img_ori = cv2.imread('/home/pi/Documents/image.jpg')
            result = pose.process(img_ori)
            img_ori = draw_landmarks(img_ori, result)
            cv2.imwrite('/home/pi/Documents/landmarked_image.jpg', img_ori)
            statelist[i] = Processor.ImageProcess(img)
            time_string = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            string_data = [time_string, int(statelist[i]), 1]
            print(string_data)
            # run(topic,string_data)
            if statelist[0] == 1 and statelist[1] == 1 and statelist[2] == 1:
                GPIO.output(LEDPin,GPIO.LOW)
                res = 1
                print("FFFFFFFFFuck Right")
            elif statelist[0] == 0 and statelist[1] == 0 and statelist[2] == 0:
                GPIO.output(LEDPin,GPIO.HIGH)
                res = 0
                print("FFFFFFFFFuck Wrong")
            else:
                print('pending')
            time.sleep(0.00001)
            msg = f'[{msg_number},{res}]'
            result = client.publish(topic, msg)
            status = result[0]
            if status == 0:
                print("Send " + msg + " to " + topic)
            else:
                print("Failed to send message")
            msg_number += 1
            
if __name__ == '__main__':
    publish_pos()
