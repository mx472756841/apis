#!/usr/bin/python3
# -*- coding: utf-8
""" 
@author: mengx@funsun.cn 
@file: app.py
@time: 2019/8/22 14:43
"""
import importlib
import os

from flask import Flask
from flask_restful import Api

from common.middlewares import before_request_func
from config import config


def add_resources(api):
    """
    将api中的resource添加到app的route中
    :param api:
    :return:
    """
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    files = os.walk(os.sep.join([curr_dir, "resources"]))
    #: 获取resources中多有定义的resources信息
    root, paths, fs = files.send(None)
    fs.remove("__init__.py")
    for file_name in fs:
        module = importlib.import_module("resources" + ".{}".format(file_name.split(".")[0]))
        resources = getattr(module, 'resources', [])
        for resource in resources:
            obj = resource['cls']
            url_rule = resource['url_rule']
            kwargs = resource.get('kwargs', {})
            api.add_resource(obj, *url_rule, **kwargs)


def create_app():
    config_name = os.getenv('FLASK_CONFIG') or 'default'
    app = Flask(__name__)

    #: app日志处理
    app.config.from_object(config[config_name])
    api = Api(app, prefix='/v1')

    #: todo 跨域访问

    #: 加载所有restful resource
    add_resources(api)

    #: 统一加载before_request
    for func in before_request_func:
        app.before_request(func)

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
