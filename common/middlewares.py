#!/usr/bin/python3
# -*- coding: utf-8
""" 
@author: mengx@funsun.cn 
@file: middlewares.py
@time: 2019/8/22 17:12
"""
import pymysql
from flask import current_app

from utils.mysql import MyDictCursor


def open_db():
    """
    打开数据库连接
    :return:
    """
    try:
        db_conn = pymysql.connect(
            host=current_app.config['DB_HOST'],
            port=int(current_app.config['DB_PORT']),
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASS'],
            db=current_app.config['DB_NAME'],
            charset="utf8mb4",
            cursorclass=MyDictCursor,
            autocommit=False
        )
        current_app.db = db_conn
    except:
        current_app.logger.exception("打开数据库失败")
        return "系统错误，稍后重试"


def close_db(resp):
    """
    关闭数据库连接
    :return:
    """
    try:
        current_app.db.close()
    except:
        current_app.logger.exception("关闭数据库失败")
    return resp


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
