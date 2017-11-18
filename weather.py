import json
import requests
import sys
import traceback
from bunch import Bunch

class LocationNotFound(Exception):
    pass


class Weather():

    def __init__(self, location = None):
        if not location:
            location = Weather.get_location()
        print('Location set to {}'.format(location))
        self.location = location
        try:
            self.location_details = Weather.get_location_details(self.location)
        except LocationNotFound as e:
            print(e)
            sys.exit()

    @staticmethod
    def get_location():
        '''Return location specified in arguments'''
        if len(sys.argv) < 2:
            print('Usage: weather.py location')
            # raise Exception('Location not specified')
            sys.exit()
        return ' '.join(sys.argv[1:])

    @staticmethod
    def get_location_details(location):
        # https://www.metaweather.com/api/
        url = 'https://www.metaweather.com/api/location/search/?query={0}'.format(location)
        response = requests.get(url)
        response.raise_for_status()
        location_details = json.loads(response.text)
        print('Received response {0}'.format(location_details))
        if not location_details:
            raise LocationNotFound('Location \'{0}\' was not found.'.format(location))
        location_details = Bunch(location_details[0])
        print('Received city details for {0}: {1}'.format(location, json.dumps(location_details)))
        return location_details


if __name__ == '__main__':
    weather = Weather('Warsaw')
    print(weather.location_details.woeid)

    # location = get_location()
    # print('Specified location: {0}'.format(location))
    #
    # city_id = get_city_woeid_(location)
    #
    # print('Received id for specified location: {0}'.format(city_id))
