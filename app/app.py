from flask import Flask
from app import config
from .view import index, gen_pass, get_my_ip, get_req, get_location

app = Flask(__name__)
app.config.update(config.dev_config)

app.add_url_rule('/', view_func=index)
app.add_url_rule('/index.html', view_func=index)

app.add_url_rule('/password-gen.html', view_func=gen_pass)

app.add_url_rule('/your-ip.html', view_func=get_my_ip)

app.add_url_rule('/show-req.html', view_func=get_req)

app.add_url_rule('/show-location.html', view_func=get_location)
