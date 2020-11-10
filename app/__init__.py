from gevent import monkey
monkey.patch_all()
from flask import Flask
#from gevent import wsgi
from gevent import pywsgi

app = Flask(__name__)
from app import routes


server = pywsgi.WSGIServer(('127.0.0.1', 5000), app)
server.serve_forever()