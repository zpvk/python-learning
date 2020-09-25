import urllib.request, urllib.parse, urllib.error
import json
 
fh = open('urlgeo.txt', 'w')
 
# Note that Google is increasingly requiring keys
# for this API, recheve the information from the website
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
 
while True:
    address = input('Enter location: ')
#    address = 'University of Buenos Aires'
    if len(address) < 1: break
 
    url = serviceurl + urllib.parse.urlencode(
        {'address': address})
 
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
 
    try:
        js = json.loads(data)
    except:
        js = None
 
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
 
    raw_data = json.dumps(js, indent=4)
    fh.write(raw_data+'\n')
    fh.close()
 
    # load the file information into data
    fh = open('urlgeo-1.txt')
    data = fh.read()
    fh.close()
 
    # extract the inforamtion from Json
    raw_handle = json.loads(data)
    # print(len(raw_handle)), two keys are status and results
    handle_results = raw_handle['results']
   
    #print(type(handle_results),len(handle_results)), 
    #this is a list with only one value
 
    handle_address = handle_results[0]
    place_id = handle_address['place_id']
    print(place_id)
