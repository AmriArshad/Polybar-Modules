#!/bin/python
# -*- coding: utf-8 -*-

import requests

REQ = requests.get("https://etherchain.org/api/gasnow")
try:
    # HTTP CODE = OK
    if REQ.status_code == 200:
      data = REQ.json()["data"]
      rapid = round(int(data["rapid"]) * 10 ** -9)
      fast = round(int(data["fast"]) * 10 ** -9)
      print("{} Gwei".format(rapid, fast))
    else:
        print("Error: BAD HTTP STATUS CODE " + str(REQ.status_code))
except (ValueError, IOError):
    print("Error: Unable print the data")