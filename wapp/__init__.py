# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api, reqparse

from wapp.controller.buddy import Buddy

webapp = Flask(__name__)
rest_api = Api(webapp)
request_parser = reqparse.RequestParser

# 添加资源
rest_api.add_resource(Buddy,
                      '/buddy/<string:buddy_id>',
                      '/buddy')

