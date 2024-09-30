import urllib.request
import json


def address(lat,lon):
  key='bdc_33777b7032944d3492a7e79e63bd3084'
  url=f'https://api-bdc.net/data/reverse-geocode?latitude={lat}&longitude={lon}&localityLanguage=en&key={key}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result
  