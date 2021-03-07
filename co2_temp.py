from CO2Meter import *
from datetime import datetime

import time
sensor = CO2Meter("/dev/hidraw0")
while True:
    time.sleep(2)
    
    now = datetime.now()
    now_str = now.strftime('%Y/%m/%d %H:%M:%S')

    sensor_data = sensor.get_data()
    if 'temperature' not in sensor_data.keys():
        continue
    temperature = sensor_data['temperature']
    if 'co2' not in sensor_data.keys():
        continue
    co2 = sensor_data['co2']
    print('{},{},{}'.format(now_str,temperature,co2))
    break
