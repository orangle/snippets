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


def ts_to_datestr(ts, fmt="%Y-%m-%d %H:%M"):
    """可读性"""
    return ts_to_datetime(ts).strftime(fmt)


def timestr_to_ts(timestr):
    """apid的输入参数格式"""
    dt = datetime.strptime(timestr, "%Y-%m-%d:%H:%M")
    return datetime_to_ts(dt)