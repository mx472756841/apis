#!/usr/bin/python3
# -*- coding: utf-8
"""
@author: mengx@funsun.cn
@file: auth.py
@time: 2019/8/22 14:54
"""
from flask import request, current_app

from resources.base import BaseResource


class User(BaseResource):
    """
    用户相关操作
    """

    def get(self):
        """
        查询用户列表
        :return:
        """
        try:
            page = int(request.args.get("page", 1))
            limit = int(request.args.get("limit", 20))
            sort = request.args.get("sort", "-id")
            offset = (page - 1) * limit
            with current_app.db.cursor() as cousor:
                sql = """
                    select id, phone, nickname, balance, create_time
                    from mmc_user_info
                    order by %s
                    limit %s, %s
                """
                cousor.execute(sql, [sort, offset, limit])
                data = cousor.fetchall()

                sql = """
                    select count(*) cnt from mmc_user_info 
                """
                cousor.execute(sql)
                total = cousor.fetchone()

            return self.success({"items": data, "total": total['cnt']})
        except:
            current_app.logger.exception("查询用户列表异常")
            return self.fail("系统异常，稍后重试")


resources = [
    {
        "cls": User,
        "url_rule": ['/user/list'],
        "kwargs": {
            "endpoint": "real_user"
        }
    },
]
