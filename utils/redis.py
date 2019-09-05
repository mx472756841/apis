# -*- coding: utf-8 -*-
"""
@author: mengx@funsun.cn
@file: redis.py
@time: 2019/09/05 09:55
"""
import redis


class RedisClient(object):
    _client = None

    def __init__(self, host, port, password, db):
        if self._client is None:
            self._create_redis_client(host, port, db, password)

    @classmethod
    def _create_redis_client(cls, host, port, db, password):
        """
        创建连接
        :return:
        """
        # not to use the connection pooling when using the redis-py client in Tornado applications
        # http://stackoverflow.com/questions/5953786/how-do-you-properly-query-redis-from-tornado/15596969#15596969
        RedisClient._client = redis.StrictRedis(host=host, port=port, db=db, password=password)

    @classmethod
    def get_client(cls, host, port, db, password):
        if RedisClient._client is None:
            cls._create_redis_client(host, port, db, password)
        return RedisClient._client
