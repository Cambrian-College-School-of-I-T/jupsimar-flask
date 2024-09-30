import urllib.request
import json

def get_weather(lat,lon):
  key='30a9373ba7126f3a8fccdd6f1322e965'
  url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result
  