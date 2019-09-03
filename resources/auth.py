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
        return self.success('admin-token')


resources = [
    {
        "cls": Auth,
        "url_rule": ['/user/login']
    }

]
