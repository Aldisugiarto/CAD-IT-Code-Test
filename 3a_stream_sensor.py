#---------------------------------------------------Sensor Aggregation---------------------------------------------------#
# Author    : Aldi Sugiarto
# Date      : April,8th 2021
# Version   : 1.0
# Email     : aldisugiarto@gmail.com
#---------------------------------------------------Sensor Aggregation---------------------------------------------------#

#---------------------------------------------------Import Module---------------------------------------------------#
# Import library
import json
import requests
import pandas as pd
from datetime import datetime
import numpy as np
import time
import random
# --------------------------------------------------------------------------------------------------------- #

#---------------------------------------------------Dictionary---------------------------------------------------#
# Set variable default value
log_time = 2               # In minutes
rooms = ['roomArea1',   # RoomArea data
        'roomArea2',
        'roomArea3',
        'roomArea4',
        'roomArea5']
temp = 0
hum = 0
data_sensors = []
index = 1
# --------------------------------------------------------------------------------------------------------- #

#---------------------------------------------------Algortihm---------------------------------------------------#
# Please force stop from code editor to STOP the process
while(True):
    timestamp = datetime.timestamp(datetime.now())
    temp = random.uniform(17.0,27.0)
    hum = random.uniform(87.0,97.0)
    sensor = {'id':index,
              'timestamp':timestamp,
              'temperature':temp,
              'humidity':hum}

    data_sensors.append(sensor)
    time.sleep(log_time*60)
    index += 1
    with open("log_sensor.json","w") as write_file:
        json.dump(data_sensors, write_file, indent = 4)
    print(data_sensors)
# --------------------------------------------------------------------------------------------------------- #