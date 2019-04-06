#!/bin/bash
# you need to have python3 + pip installed on your os but should be by default..
sudo apt-get update && sudo apt-get upgrade
sudo apt-get -y install unzip
pip install paho-mqtt AWSIoTPythonSDK

# copy connect_device_package.zip to your raspi:
# scp bigdata_raspi_weather/connect_device_package.zip pi@192.168.0.12:/tmp
mkdir -p /opt/aws_connect
cp connect_device_package.zip /opt/aws_connect
unzip /opt/aws_connect/connect_device_package.zip
/opt/aws_connect/start.sh
