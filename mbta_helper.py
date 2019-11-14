import urllib.request
import urllib.parse
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://open.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "aAEdyzcmLAVQ1r4cxhzt5IKM0la4xh6E"
MBTA_API_KEY = "7e3f9835ebae45728f5f15e18c3da85a"

# A little bit of scaffolding if you want to use it

url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'

def get_json(url):
    """
    Given a prop erly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    MAPQUEST_API_KEY= 'aAEdyzcmLAVQ1r4cxhzt5IKM0la4xh6E'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)
    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    parsed = {'key' : MAPQUEST_API_KEY, 'location' : place_name}
    parsed_url = urllib.parse.urlencode(parsed)
    # print (parsed_url)
    url = f'http://www.mapquestapi.com/geocoding/v1/address?{parsed_url}'
    # print (url)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint(response_data)
    return response_data["results"][0]["locations"][0]['displayLatLng']


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&filter[radius]=1&sort=distance&page[limit]=1'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)
    name, wheel_chair = response_data["data"][0]["attributes"]['name'], response_data["data"][0]["attributes"]['wheelchair_boarding']
    if wheel_chair == 2:
        wheel_chair = 'Inaccessible'
    elif wheel_chair == 1:
        wheel_chair = 'Accessible'
    else:
        wheel_chair = 'No Information'
    return name, wheel_chair



def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    dictionary = get_lat_long(place_name)
    latitude = dictionary['lat']
    longitude = dictionary['lng']
    return get_nearest_station(latitude,longitude)


def main():
    """
    You can put all the functions here
    """
    # print(get_json(url))
    location = input('Please enter the name of a place:')
    print(get_lat_long(location))
    print(find_stop_near(location))
    
if __name__ == '__main__':
    main()