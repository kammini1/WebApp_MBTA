# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://open.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "aAEdyzcmLAVQ1r4cxhzt5IKM0la4xh6E"
MBTA_API_KEY = "7e3f9835ebae45728f5f15e18c3da85a"


# A little bit of scaffolding if you want to use it

import urllib.request
import json
from pprint import pprint
place_name=input('enter a location.')
parsed={'key':MAPQUEST_API_KEY, 'location':place_name}
parsed_url=urllib.parse.urlencode(parsed)
url=f'http://www.mapquestapi.com/geocoding/v1/address?{parsed_url}'
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)


def get_json(url):
    """
    Given a prop erly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)

get_json(url)

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    
    print(response_data["results"][0]["locations"][0]['displayLatLng'])

get_lat_long(place_name)

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    parsed={'key':MBTA_API_KEY, 'latitude':latitude, 'longitude':longitude, 'data':response_data, 'station_name':parent_station,'wheelchair_accessible':wheelchair_accessible}
    parsed_url=urllib.parse.urlencode(parsed)
    url=f'https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index?{parsed_url}'
    f=urllib.request.urlopen(url)
    print(response_data["results"][0]["station_name"][0]["wheelchair_accessible"])

get_nearest_station(42.9,-37.9)

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    parsed={'key':MBTA_API_KEY, 'place_name':place_name,'data':response_data, 'station_name':parent_station,'wheelchair_accessible':wheelchair_accessible}
    parsed_url=urllib.parse.urlencode(parsed)
    url=f'https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index?{parsed_url}'
    f=urllib.request.urlopen(url)
    print(response_data["results"][0]["station_name"][0]["wheelchair_accessible"])

find_stop_near(place_name)

def main():
    """
    You can put all the functions here
    """
    


if __name__ == '__main__':
    main()
