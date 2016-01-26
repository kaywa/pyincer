# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext import restful

container = Flask(__name__)

api = restful.Api(container)