#!/bin/python
# -*- coding: utf-8 -*-

import requests
from datetime import datetime

CITY = "Auckland"
COUNTRY = "NZ"
METHOD = 3

REQ = requests.get("https://api.aladhan.com/v1/timingsByCity?city={}&country={}&method={}".format(CITY, COUNTRY, METHOD))
try:
    # HTTP CODE = OK
    if REQ.status_code == 200:
      timings = REQ.json()["data"]["timings"]
      
      # remove extra timings
      del timings['Sunset']
      del timings['Imsak']
      del timings['Midnight']
      
      current = datetime.now().time().strftime("%H:%M")

      for time in timings.items():
        # format time
        formatted_time = datetime.strptime(time[1], "%H:%M").time().strftime("%H:%M") 
        # check for next timings
        if (current < formatted_time):
          # calculate difference
          tdelta = str(datetime.strptime(formatted_time,'%H:%M') - datetime.strptime(current,'%H:%M')).split(":")

          hours = tdelta[0]
          minutes = tdelta[1]

          print("{} in {}:{}".format(time[0], hours, minutes))
          break
    else:
        print("Error: BAD HTTP STATUS CODE " + str(REQ.status_code))
except (ValueError, IOError):
    print("Error: Unable print the data")