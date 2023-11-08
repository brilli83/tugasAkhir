import paho.mqtt.publish as publish
import json
import base64
import random

# f = open("mqtt.png", "rb")
def send_image(path):
    filecontent = ""
    # base64.b64encode(filecontent)
    with open(path, "rb") as image_file:
        filecontent = base64.b64encode(image_file.read())
    # byteArr = bytearray(filecontent)
    # byteArr = "haha"
    publish.single('/raspberry/smoke', filecontent, qos=0,
               hostname='broker.hivemq.com')
    
def send_object_name(object_name):
    filecontent = ""
    # base64.b64encode(filecontent)
    # with open(path, "rb") as image_file:
    filecontent = object_name
    # byteArr = bytearray(filecontent)
    # byteArr = "haha"
    publish.single('/raspberry/objectname', filecontent, qos=0,
               hostname='broker.hivemq.com')
