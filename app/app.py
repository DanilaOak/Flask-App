from flask import Flask
from app.config import DevConfig
from app.view import index, get_req, UserReg, get_my_ip, location, weather, location, PasswordGen, AllCustomers, FilterByName, FilterCityCompanyState, AwesomeUrl

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

app.add_url_rule('/show-customers.html', view_func=AllCustomers.as_view('all customers'))

app.add_url_rule('/filter-by-name.html', view_func=FilterByName.as_view('filter customers by name'))

app.add_url_rule('/filter-company-city-state.html',
                 view_func=FilterCityCompanyState.as_view('filter city, company and state'))

app.add_url_rule('/awesome-url.html',
                 view_func=AwesomeUrl.as_view('awesome + json'))

