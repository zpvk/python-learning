# -*- coding: utf-8 -*-
# @Author: Rohan Kumara
# @Date:   2020-10-27 23:59:27
# @Last Modified by:   Rohan Kumara
# @Last Modified time: 2020-10-27 23:59:27


import requests
# You need to install the requests module to use this code
import json

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
else:

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json'
    if len(address) < 1:
        break
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json'
while True:
    address = input('Enter location: ')
    if api_key is not False:
        payload['key'] = api_key
    
    payload = dict()
    payload['address'] = address
    if api_key is not False: payload['key'] = api_key


    r = requests.get(serviceurl, params=payload)
    print('Retrieved', r.url)
    data = r.text
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

