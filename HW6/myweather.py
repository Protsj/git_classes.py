import json
import weather_errors as werror
from urllib.request import urlopen

ENDPOINT_URL = 'https://api.openweathermap.org/data/2.5/weather?{params}'
API = '33c014a38763066f0f4cc528ec132a59'

def req_url(**kwargs):
    params = '&'.join([f'{k}={v}' for k, v in kwargs.items()])
    return ENDPOINT_URL.format(params=params)

def get_curtemp(response):
    current = response['main']
    current_temp = float(round((current['temp'] - 273.15), 2))
    return current_temp

def make_request(url):
    response = urlopen(url)
    data = response.read()
    data = data.decode('utf-8')
    result = json.loads(data)
    return result

def request_curtemp(lon, lat):
    url = req_url(lon=lon, lat=lat, appid=API)
    response = make_request(url)
    temp = get_curtemp(response)
    return temp

GEO_URL = ('https://api.openweathermap.org/geo/1.0/direct?q={city}'
           '&appid=33c014a38763066f0f4cc528ec132a59&units=metric')

class City():

    def __init__(self, city):
        self.city = city

    def get_coordinates(self):
        try:
            url = GEO_URL.format(city={self.city})
            data = make_request(url)
            self.lat = data[0]['lat']
            self.lon = data[0]['lon']
            print(f'City: {self.city}\nLongtitude: {self.lon}\nLatitude: {self.lat}')
        except IndexError:
            raise werror.NoCityFoundError()
        except TypeError:
            raise werror.CityNameError()


class Weather(City):
    def __init__(self, city):
        self.city = city
    
    def get_temperature(self):
        try:
            url = req_url(lon=self.lon, lat=self.lat, appid=API)
            response = make_request(url)
            temp = get_curtemp(response)
            _deg = '\u00b0'
            print(f'\nTemperature: {temp}{_deg}C')

        except KeyError:
            raise werror.KeyError()


mycity = Weather('London')
mycity.get_coordinates()
mycity.get_temperature()
    