#! /usr/bin/env python3
# weatherTweet.py - sends a tweet with current weather

import requests, bs4
from twython import Twython
from auth import(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
) 


twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
    

def getWeather():
    global temp
    res = requests.get('http://forecast.weather.gov/MapClick.php?lat=41.79650711791027&lon=-87.97108737927834#.V36qDLgrLic')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    x = soup.select('#current_conditions-summary > p.myforecast-current-lrg')
    xText = x[0].getText()
    temp = xText[:2]
    return temp





getWeather()
weather = "The Current Temperature outside in #Chicago is %s degrees Fahrenheit. #RaspberryPi" % (temp)
twitter.update_status(status=weather)



