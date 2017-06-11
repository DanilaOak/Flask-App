from flask import Flask
from app.config import DevConfig
from app.view import index, get_my_ip, get_req, location, weather, UserReg, PasswordGen

app = Flask(__name__)
app.config.from_object(DevConfig)

app.add_url_rule('/', view_func=index)
app.add_url_rule('/index.html', view_func=index)

app.add_url_rule('/password-gen.html', view_func=PasswordGen.as_view('password generator'))

app.add_url_rule('/your-ip.html', view_func=get_my_ip)

app.add_url_rule('/show-req.html', view_func=get_req)

app.add_url_rule('/show-location.html', view_func=location)

app.add_url_rule('/weather-api.html', view_func=weather)

app.add_url_rule('/reg-user.html', view_func=UserReg.as_view('registration'))
