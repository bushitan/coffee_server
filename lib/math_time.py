#coding:utf-8
import time
import datetime
def valid_day(second ):
    now = datetime.datetime.now()
    now_stamp = time.mktime(now.timetuple())
    valid = now_stamp + second
    return datetime.datetime.fromtimestamp(valid)
