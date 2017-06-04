from flask import render_template, request
from .utils import gen_password


def index():
    return render_template('index.html', title='Hello World')

def gen_pass():
    context = {'password': gen_password(), 'title': 'Password Generator'}
    return render_template('password-gen.html', data=context, title=context['title'])

def get_my_ip():
    ip = {"ip2": request.headers.get('X-Forwarded-For')}
    return render_template("your-ip.html", user_ip=ip, title='Your IP')


