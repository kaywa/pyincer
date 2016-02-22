# -*- coding: utf-8 -*-


from wapp.decorator.sign import Decorators
from flask_restful import Resource, fields, abort, Api
from flask import request

resource_fields = {'sign': fields.String(default='default_sign')}

class Buddy(Resource):

    def __init__(self):
        pass

    @Decorators.SignCheck
    def get(self, buddy_id= '0'):
        '''
        查询指定用户的详情
        :return:
        '''
        print('restful get:' + buddy_id)
        return {'data':'hello get test!'+buddy_id}, 200


    @Decorators.SignCheck
    def put(self, buddy_id='0'):
        print('restful put:'+buddy_id)
        return {"data", 'hello put test'+buddy_id}, 200
