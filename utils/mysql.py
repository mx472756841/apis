# -*- coding: utf-8 -*-
import decimal
import logging
import time
from datetime import datetime

from pymysql.cursors import DictCursor

logger = logging.getLogger(__name__)


class MyDictCursorMix(object):
    def _conv_row(self, row):
        def translate_type(value):
            if isinstance(value, datetime):
                return time.mktime(value.timetuple())
            elif isinstance(value, decimal.Decimal):
                return float(value)
            else:
                return value

        if row is None:
            return None
        return self.dict_type(zip(self._fields, map(translate_type, row)))


class MyDictCursor(MyDictCursorMix, DictCursor):
    """自定义Cursor,对于数据库直接获得的数据,无法序列化的转换"""
