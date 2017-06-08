import string
import random
import geoip2.database
from flask import request
import json
import urllib


def gen_password(size=8):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(size))


def get_location():
    reader = geoip2.database.Reader('GeoLite2-City.mmdb')
    if request.headers.get('X-Forwarded-For') != None:
        ip = request.headers.get('X-Forwarded-For')
    else:
        ip = '46.98.209.171'  # test value
    response = reader.city(ip)
    info = {
        'IP Address': ip,
        'Country': response.country.name,
        'City': response.city.name,
        'City ID': response.city.geoname_id,
        'Postal Code': response.postal.code,
        'Location Latitude': response.location.latitude,
        'Location Longitude': response.location.longitude
    }
    print(response.city.geoname_id)
    reader.close()
    return info

def get_weather():
    user_info = get_location()
    url = 'http://api.weatherunlocked.com/api/current/{},{}?app_id=93a259af&app_key=3bfb8f6927fc76e827be0237be7c8c5b'.format(
            user_info['Location Latitude'], user_info['Location Longitude'])
    w = urllib.request.urlopen(url)
    json_string = w.read()
    parsed_json = json.loads(json_string)
    result = {
        'Weather Description': parsed_json['wx_desc'],
        'Temperature': parsed_json['temp_c'],
        'Feel like Temperature': parsed_json['feelslike_c'],
        'Wind Speed(kilometers per hour)': parsed_json['windspd_kmh'],
        'Pressure(millibars)': parsed_json['slp_mb']
    }
    w.close()
    print(parsed_json)
    return result

if __name__ == '__main__':
    print(gen_password(20))
