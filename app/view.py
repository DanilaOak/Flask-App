from flask import render_template, request
from .utils import gen_password, get_location, get_weather
import urllib



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

def location():
    return render_template('show-location.html', user_info=get_location(), title='Your Location')

def weather():
    weather_info = get_weather()
    return render_template('weather-api.html', weather_info=weather_info, title='Weather Info')
