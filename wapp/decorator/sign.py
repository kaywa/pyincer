# -*- coding: utf-8 -*-
from flask import request

class Decorators:
    @staticmethod
    def SignCheck(M):
        def wrapper(*args, **kwargs):
            print('wrapper is execute!')
            sign_param = request.args.get('sign')
            print('sign_param:'+sign_param)
            return M(*args, **kwargs)
        return wrapper
