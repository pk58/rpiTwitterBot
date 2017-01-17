# !/usr/bin/env python3
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


def doSpeedTest():
    resDict = {'ping':'', 'down':'', 'up':''}
    global result
    result = os.popen("/usr/local/bin/speedtest-cli --simple").read()
    return result
## CREATE A DICTIONARY AND FILL IT WITH THE RESULTS

doSpeedTest()


# ['Ping: 21.446ms', 'Download: 88.61 Mbit/s', Upload: 11.90 Mbit/s', ""]
i = datetime.now()
now = i.strftime('%H:%M:%S')
message =  'Speedtest result at ' + now + 'hrs:           ' + result + ' #RaspberryPi #SpeedTest'

print(message)
twitter.update_status(status=message)
