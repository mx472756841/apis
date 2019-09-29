#!/usr/bin/python3
# -*- coding: utf-8
"""
@author: mengx@funsun.cn
@file: auth.py
@time: 2019/8/22 14:54
"""

from resources.base import BaseResource


class Device(BaseResource):
    """
    设备相关操作
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
        "cls": Device,
        "url_rule": ['/device/list']
    },
]
