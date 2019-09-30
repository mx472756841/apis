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
            phone = request.args.get("phone", None)
            offset = (page - 1) * limit
            with current_app.db.cursor() as cousor:
                where_sql = ""
                if phone:
                    where_sql = " where phone = %s"

                sql = """
                    select id, phone, nickname, balance, create_time
                    from mmc_user_info
                    {}
                    order by %s
                    limit %s, %s
                """.format(where_sql)
                cousor.execute(sql, [phone, sort, offset, limit] if where_sql else [sort, offset, limit])
                data = cousor.fetchall()

                sql = """
                    select count(*) cnt from mmc_user_info {}
                """.format(where_sql)
                if where_sql:
                    cousor.execute(sql, phone)
                else:
                    cousor.execute(sql)
                total = cousor.fetchone()

            return self.success({"items": data, "total": total['cnt']})
        except:
            current_app.logger.exception("查询用户列表异常")
            return self.fail("系统异常，稍后重试")


class Charge(BaseResource):
    def get(self):
        """
        查询用户充值流水列表
        :return:
        """
        try:
            page = int(request.args.get("page", 1))
            limit = int(request.args.get("limit", 20))
            sort = request.args.get("sort", "-a.id")
            phone = request.args.get("phone", None)
            offset = (page - 1) * limit
            with current_app.db.cursor() as cousor:
                where_sql = ""
                if phone:
                    where_sql = " AND b.phone = %s"

                sql = """
                    SELECT
                        a.id, b.phone, a.user_id, c.location as device_name,
                        a.order_no, a.interface_number as interface,
                        a.expect_time, a.expect_amount, a.device_id,
                        a.actual_time, a.actual_amount, a.actual_power,
                        a.status, a.update_time, a.create_time
                    FROM
                        mmc_user_charge_info a,
                        mmc_user_info b,
                        mmc_device_info c 
                    WHERE
                        a.user_id = b.id 
                        AND a.device_id = c.id
                        AND a.is_delete = 0
                        {}
                    order by {}
                    limit %s, %s
                """.format(where_sql, sort)
                cousor.execute(sql, [phone, offset, limit] if where_sql else [offset, limit])
                data = cousor.fetchall()

                sql = """
                    select count(*) cnt from mmc_user_charge_info a, mmc_user_info b 
                    where a.is_delete = 0 
                    AND a.user_id = b.id {} 
                """.format(where_sql)
                if where_sql:
                    cousor.execute(sql, phone)
                else:
                    cousor.execute(sql)
                total = cousor.fetchone()

            return self.success({"items": data, "total": total['cnt']})
        except:
            current_app.logger.exception("查询充值流水列表异常")
            return self.fail("系统异常，稍后重试")


resources = [
    {
        "cls": User,
        "url_rule": ['/user/list'],
        "kwargs": {
            "endpoint": "real_user"
        }
    },
    {
        "cls": Charge,
        "url_rule": ['/user_charge/list'],
        "kwargs": {
            "endpoint": "charges"
        }
    },
]
