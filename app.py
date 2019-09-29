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
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from common.middlewares import before_request_func, after_request_func
from config import config

db = SQLAlchemy()


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

    #: app配置环境处理
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #: 数据库处理
    db.init_app(app)

    #: 加载所有restful resource
    api = Api(app)
    add_resources(api)
    #: 统一加载before_request
    for func in before_request_func:
        app.before_request(func)

    #: 统一加载after_request
    for func in after_request_func:
        app.after_request(func)

    #: 跨域访问, 指定允许的请求地址 直接指定参数，也可以指定单独path的跨域请求处理
    #: https://flask-cors.readthedocs.io/en/latest/
    CORS(app, origins=app.config['CORS_ORIGINS'], max_age=86400)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(port=8801)
