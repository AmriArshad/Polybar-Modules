#!/bin/python
# -*- coding: utf-8 -*-

import requests
from datetime import datetime

CITY = "Auckland"
COUNTRY = "NZ"
METHOD = 3

def tdelta(time1, time2):
  # calculate difference
  tdelta = str(datetime.strptime(time2,'%H:%M') - datetime.strptime(time1,'%H:%M')).split(":")

  if len(tdelta[0]) > 1:
    hours = tdelta[0][-1]
  else:
    hours = tdelta[0]

  minutes = tdelta[1]

  return hours, minutes

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
          hours, minutes = tdelta(current, formatted_time)
          print("{} in {}:{}".format(time[0], hours, minutes))
          break
        else:
          # edge case for time between isha and midnight
          fajr = timings['Fajr']
          hours, minutes = tdelta(current, fajr)
          print("{} in {}:{}".format(time[0], hours, minutes))
          break
    else:
        print("Error: BAD HTTP STATUS CODE " + str(REQ.status_code))
except (ValueError, IOError):
    print("Error: Unable print the data")