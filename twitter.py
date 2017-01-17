#!/usr/bin/env python3
from datetime import datetime
import sys
import os
from twython import Twython
from auth import(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret) 


twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

i = datetime.now()
cmd = '/opt/vc/bin/vcgencmd measure_temp' 
now = i.strftime('%H:%M:%S')
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]
fTemp = (float(temp)*float(1.8)) + 32
fTemp = round(fTemp, 1)
message = 'Rasberry Pi Processor Temp: ' + str(fTemp) +' degrees F  ' + 'at  ' + now + 'hrs #RaspberryPi'
twitter.update_status(status=message)
print("Tweeted: %s" % message)
