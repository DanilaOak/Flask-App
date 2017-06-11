from flask import render_template, request
from .utils import gen_password, get_location, get_weather
from flask.views import MethodView

class UserReg(MethodView):
    def get(self):
        return render_template('reg-user.html', title='REG USER')

    def post(self):
        form = request.form
        login = form['login']
        password = form['password']
        data = {'login': form['login'],
                'password': form['password']}
        return render_template('reg-user.html', data=data, title='REG USER')


class PasswordGen(MethodView):
    def get(self):
        return render_template('password-gen.html', title='Password Generator')

    def post(self):
        context = {'password': gen_password(int(request.form["Len"]))}
        return render_template('password-gen.html', data=context, title='Password Generator')


def index():
    return render_template('index.html', title='Hello World')


def get_my_ip():
    ip = {"ip2": request.headers.get('X-Forwarded-For')}
    return render_template("your-ip.html", user_ip=ip, title='Your IP')


def get_req():
    with open('requirements.txt', 'r') as r:
        req = r.read().split('\n')
    return render_template('show-req.html', requirements=req, title='Show Requirements')


def location():
    return render_template('show-location.html', user_info=get_location(), title='Your Location')


def weather():
    weather_info = get_weather()
    return render_template('weather-api.html', weather_info=weather_info, title='Weather Info')
