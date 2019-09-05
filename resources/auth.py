#!/usr/bin/python3
# -*- coding: utf-8
""" 
@author: mengx@funsun.cn 
@file: auth.py
@time: 2019/8/22 14:54
"""

from resources.base import BaseResource


class Auth(BaseResource):

    def post(self):
        """
        用户登录返回Token信息
        :return:
        """
        sql = """
            
        """
        return self.success({'token': 'admin-token'})


class User(BaseResource):

    def get(self):
        """
        查询用户信息
        根据token
        :return:
        """
        data = {
            "roles": ['admin'],
            "introduction": 'I am a super administrator',
            "avatar": 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
            "name": 'Super Admin'
        }
        return self.success(data)


class UserLogout(BaseResource):
    """
    用户登出
    """

    def post(self):
        """
        用户登录返回Token信息
        :return:
        """
        return self.success('success')


class UserRoutes(BaseResource):
    """
    获取用户的routes
    """
    def get(self):
        return self.success({})


resources = [
    {
        "cls": Auth,
        "url_rule": ['/user/login']
    },
    {
        "cls": User,
        "url_rule": ['/user/info']
    },
    {
        "cls": UserLogout,
        "url_rule": ['/user/logout']
    },
    {
        "cls": UserRoutes,
        "url_rule": ['/user/routes']
    },
]
