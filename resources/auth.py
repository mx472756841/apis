#!/usr/bin/python3
# -*- coding: utf-8
""" 
@author: mengx@funsun.cn 
@file: auth.py
@time: 2019/8/22 14:54
"""
from flask import request, current_app

from app import db
from resources.base import BaseResource
from utils.utils import get_uuid


class Auth(BaseResource):

    def post(self):
        """
        用户登录返回Token信息
        :return:
        """
        user_info = request.json
        username = user_info.get('username')
        password = user_info.get('password')
        if not username or not password:
            return self.fail("用户名和密码不可以为空")

        sql = """
            select id as user_id, password, is_active
            from base_user_info
            where username = :username
        """
        cur = db.session.execute(sql, {"username": username})
        query_user = cur.fetchone()
        if not query_user:
            return self.fail("用户不存在")

        if not query_user['is_active']:
            return self.fail("该用户已经被锁定，请联系系统管理员")

        # todo 密码进行加密处理
        if query_user['password'] != password:
            return self.fail("密码错误，请检查后重试")

        # todo 连续错误次数锁定账号
        # todo 连续错误，要求前端输入验证码

        # 生成token，返回前端
        token = get_uuid()
        token_key = current_app.config['TOKEN_KEY'] % token
        current_app.redis.setex(token_key, 30 * 24 * 60 * 60, query_user['user_id'])
        return self.success({'token': token})


class User(BaseResource):

    def get(self):
        """
        查询用户信息
        根据token
        :return:
        """
        data = {
            "roles": ['editor'],
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
        data = [
            {
                'path': '/icon',
                'name': 'IconManage',
                'meta': {
                    'roles': ['admin', 'editor']
                },
                'children': [
                    {
                        'path': 'index',
                        'name': 'Icons',
                        'meta': {
                            'title': 'Icons',
                            'icon': 'icon',
                            'noCache': True,
                            'roles': ['admin', 'editor']
                        }
                    }
                ]
            }
        ]
        return self.success(data)


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
