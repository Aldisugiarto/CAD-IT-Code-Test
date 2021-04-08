#---------------------------------------------------Sensor Aggregation---------------------------------------------------#
# Author    : Aldi Sugiarto
# Date      : April,7th 2021
# Version   : 1.0
# Email     : aldisugiarto@gmail.com
#------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------Import module---------------------------------------------------#
# Import library
import json
import requests
import pandas as pd
from datetime import datetime
from pandas.io.json import json_normalize
#------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------Variable set value---------------------------------------------------#
index=0
#------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------Class or function---------------------------------------------------#
def convert_timestamp(times):
    sTime = str(times)
    newTimes = int(sTime[0:10])
    dt_object = datetime.fromtimestamp(newTimes)
    return dt_object.strftime("%x")
#------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------Algorithm---------------------------------------------------#
# Open json file
path = "JSON Files/sensor_data.json"
f = open(path)
# Assign data to new variable
data_sensor = json.load(f)
data_sensor = data_sensor['array'] #Change dict to list
# Iteration for data sensor
for sensor in data_sensor:
    new_date = {'timestamp':convert_timestamp(sensor['timestamp'])} #Convert timestamp to date and assig to new dict
    sensor.update(new_date) #Update sensor data in dict
    data_sensor[index].update(sensor) #Update sensor data in list
    index += 1
# Conversion from json to dataframe
sensors = json_normalize(data_sensor)
sensors = sensors.drop('id',axis=1) #Drop 'id' column
# Groupby timestamp and roomArea, then calculate sensors for min,max,median,and mean
data_sensors_math = sensors.groupby(['timestamp','roomArea']).agg(['min','max','median','mean'])
# Print the new value from group data
print(data_sensors_math)
#--------------------------------------------------------------Thank You----------------------------------------------------------#