#---------------------------------------------------Statistics Sensor---------------------------------------------------#
# Author    : Aldi Sugiarto
# Date      : April,7th 2021
# Version   : 1.0
# Email     : aldisugiarto@gmail.com
#-----------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------Import Module---------------------------------------------------#
# Import library
import json
import requests
import time
import numpy as np
#-----------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------Class or function---------------------------------------------------#
# Display function
def display(sensor,min,max,mean,med):
    print('#----------------',sensor,'--------------#')
    print('Min. value: ',min)
    print('Max. value',max)
    print('Mean value',mean)
    print('Median value',med)
#-----------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------Variable set value---------------------------------------------------#
log_time = 15    #In minutes
temp=[]
hum=[]
#-----------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------Algorithm---------------------------------------------------#
# *****Please force stop from code editor to STOP the process
# Open specified file path
path = "log_sensor.json"
f = open(path)
# Assign to new variable
data_sensor = json.load(f)
# while true until dead
while(True):
    time.sleep(log_time*60) #log every log_time
    # Get sensor data
    for sensor in data_sensor:
        # Add to list variable each sensor
        temp.append(sensor['temperature'])
        hum.append(sensor['humidity'])

    # Assign min,max,mean, and median to variable (sometimes will need the variable)
    # Temperature sensor
    min_temp = np.min(temp)
    max_temp = np.max(temp)
    mean_temp = np.mean(temp)
    median_temp = np.median(temp)
    # Call display function to print the value
    display('Temperature',min_temp,max_temp,mean_temp,median_temp)

    # Humidity sensor
    min_hum = np.min(hum)
    max_hum = np.max(hum)
    mean_hum = np.mean(hum)
    median_hum = np.median(hum)
    # Call display function to print the value
    display('Humidity',min_hum,max_hum,mean_hum,median_hum)
#-----------------------------------------------------------------------------------------------------------------------#