#
############################################

# importing libraries
import paho.mqtt.client as paho
import os
import json
from datetime import date, datetime
import socket
import ssl
from time import sleep
from random import uniform

connflag = False

def on_connect(client, userdata, flags, rc):                # func for making connection
    global connflag
    print ("Connected to AWS")
    connflag = True
    print ("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg):                      # Func for Sending msg
    print (msg.topic+" "+str(msg.payload))

#def on_log(client, userdata, level, buf):
#    print (msg.topic+" "+str(msg.payload))

mqttc = paho.Client()                                       # mqttc object
mqttc.on_connect = on_connect                               # assign on_connect func
mqttc.on_message = on_message                               # assign on_message func
#mqttc.on_log = on_log

#### Change following parameters ####
awshost = "a17tm7cjhqrsqq-ats.iot.us-west-2.amazonaws.com"      # Endpoint
awsport = 8883                                              # Port no.
clientId = "RasberryPi"                                     # Thing_Name
thingName = "RasberryPi"                                    # Thing_Name
caPath = "root-CA.crt"                                      # Root_CA_Certificate_Name
certPath = "RasberryPi.cert.pem"                            # <Thing_Name>.cert.pem
keyPath = "RasberryPi.private.key"                          # <Thing_Name>.private.key

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  # pass parameters

mqttc.connect(awshost, awsport, keepalive=60)               # connect to aws server

mqttc.loop_start()                                          # Start the loop



while 1==1:
    data = {}
    sleep(60)
    if connflag == True:
        
        date_tmp=datetime.utcnow() 
        data["timestamp"] = date_tmp.strftime('%Y-%m-%dT%H:%M:%SZ') 
        data["temperature"] = uniform(5.0,40.0)
        payload=json.dumps(data)
        print (payload)
        mqttc.publish("sensordata", payload, qos=1)        # topic: temperature # Publishing Temperature values

    else:
        print("waiting for connection...")

