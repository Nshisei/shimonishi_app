#!/usr/bin/env python
# Note:
# ds18b20's data pin must be connected to pin7.
# Reads temperature from sensor and prints to stdout
# id is the id of the sensor
import os
import time
def readSensor():
    for file in os.listdir("/sys/bus/w1/devices/"):
        print(file)
        if not (file.startswith("28-")):
            continue
        tfile = open("/sys/bus/w1/devices/"+file+"/w1_slave")
        text = tfile.read()
        tfile.close()
        print(text)
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        temperature = temperature / 1000
        return temperature


# Reads temperature from all sensors found in /sys/bus/w1/devices/
# starting with "28-.."

if __name__ == "__main__":
    print(readSensor())

