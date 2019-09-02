#!/usr/bin/python3
# -*- coding: utf-8
"""
@author: mengx@funsun.cn
@file: permission.py
@time: 2019/8/22 14:54
"""

from flask_restful import Resource


class Roles(Resource):

    def post(self):
        """
        创建校色
        :return:
        """
        return {'code': 20000, 'data': 'admin-token'}

    def get(self):
        """
        获取所有角色信息
        :return:
        """


class SingleRole(Resource):

    def put(self):
        """
        修改角色
        :return:
        """
        pass

    def delete(self):
        """
        删除角色
        :return:
        """


class Routes(Resource):
    """
    路由查询，路由添加由系统管理人员处理
    """

    def get(self):
        """
        查询所有的路由
        :return:
        """
        pass


resources = [
    {
        "cls": Roles,
        "url_rule": ['/user/login']
    }

]
