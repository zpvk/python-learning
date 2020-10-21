import requests
# You need to install the requests module to use this code
import json

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    
    payload = dict()
    payload['address'] = address
    if api_key is not False: payload['key'] = api_key


    r = requests.get(serviceurl, params=payload)
    print('Retrieved', r.url)
    data = r.text
    print('Retrieved', len(data), 'characters')

