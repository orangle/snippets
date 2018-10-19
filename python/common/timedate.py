import time
from datetime import datetime, timedelta


def st_to_datetime(st_int):
    """时间戳转化为时间
    """
    datetime.fromtimestamp(st_int)


def datetime_to_st(dt):
    """时间转换为时间戳
    """
    return time.mktime(dt.timetuple())


