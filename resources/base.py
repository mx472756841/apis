#-*- coding: utf-8 -*-
from flask_restful import Resource


class ResultMix(object):

    def success(self, data):
        return {
            "code": 20000,
            "data": data
        }

    def fail(self, message, code=40000):
        return {
            "code": code,
            "message": message
        }


class BaseResource(ResultMix, Resource):
    pass
