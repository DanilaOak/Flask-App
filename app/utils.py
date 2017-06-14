import string
import random
import geoip2.database
from flask import request
import requests
from app.config import DevConfig


def gen_password(size=8):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(size))


def get_location():
    geo_db = 'GeoLite2-City.mmdb'
    print(DevConfig.APP_DIR)
    reader = geoip2.database.Reader(DevConfig.APP_DIR + '/db_utils/' + geo_db)
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
    reader.close()
    return info

def get_weather():
    user_info = get_location()
    user_lat = user_info['Location Latitude']
    user_lon = user_info['Location Longitude']
    url = 'http://api.weatherunlocked.com/api/current/{},{}'.format(user_lat, user_lon)
    payload = {'app_id': '93a259af', 'app_key': '3bfb8f6927fc76e827be0237be7c8c5b'}
    req = requests.get(url, params=payload).text
    w = dict(item.split(':') for item in req[1:-2].replace('"', '').split(','))
    result = {
        'Weather Description': w['wx_desc'],
        'Temperature': w['temp_c'],
        'Feel like Temperature': w['feelslike_c'],
        'Wind Speed(kilometers per hour)': w['windspd_kmh'],
        'Pressure(millibars)': w['slp_mb']
    }
    return result


if __name__ == '__main__':
    print(gen_password(20))
