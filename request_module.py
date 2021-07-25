# requests module demo to get time from a API

import requests
import json

# Making a GET request
r = requests.get('http://worldtimeapi.org/api/timezone/Asia/Kolkata')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.text)




