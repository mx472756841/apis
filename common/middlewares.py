#!/usr/bin/python3
# -*- coding: utf-8
""" 
@author: mengx@funsun.cn 
@file: middlewares.py
@time: 2019/8/22 17:12
"""
from flask import current_app


def open_db():
    """
    打开数据库连接
    :return:
    """
    pass


def close_db():
    """
    关闭数据库连接
    :return:
    """
    pass


def check_auth():
    """
    除白名单url之外，其余的都需要校验是否有token
    对api而言，除了登录之外，其余的功能都需要校验是否有token
    并根据token解析出用户信息
    :return:
    """
    pass


def check_permission():
    """
    校验用户是否存在权限，从用户的token
    :return:
    """
    pass


# 请求前处理函数
before_request_func = [
    open_db,  # 打开数据库连接
    check_auth,  # 校验用户token
    check_permission  # 校验用户permission
]

# 请求后处理函数
after_request_func = [
    close_db,  # 关闭数据库连接
]
