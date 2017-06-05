from flask import render_template, request
from .utils import gen_password
import geoip2.database


def index():
    return render_template('index.html', title='Hello World')

def gen_pass():
    if request.method == 'GET':
        return render_template('password-gen.html', title='Password Generator')
    else:
        context = {'password': gen_password(int(request.form["Len"]))}
        return render_template('password-gen.html', data=context, title='Password Generator')

def get_my_ip():
    ip = {"ip2": request.headers.get('X-Forwarded-For')}
    return render_template("your-ip.html", user_ip=ip, title='Your IP')

def get_req():
    r = open('requirements.txt', 'r')
    req = r.read().split('\n')
    r.close()
    return render_template('show-req.html', requirements=req, title='Show Requirements')

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
            'Postal Code': response.postal.code,
            'Location Latitude': response.location.latitude,
            'Location Longitude': response.location.longitude
        }
    print(info)
    reader.close()
    return render_template('show-location.html', user_info=info, title='Your Location')

