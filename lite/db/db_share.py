#coding:utf-8
from lite.db.db import DBData
from lite.models import *


class DBShare(DBData):
    def __init__(self):
        super().__init__(Share)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        # print (object)
        _new = {
            "alive":object.alive,
            "receive_customer_id":object.receive_customer_id,
            "receive_customer_avatar_url":object.receive_customer.avatar_url if object.receive_customer is not None else "" ,
            "receive_customer_nick_name":object.receive_customer.nick_name if object.receive_customer is not None else "" ,
            "receive_time":object.receive_time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        return dict(_base,**_new)
if __name__ == '__main__':
    # import django
    # django.setup()
    # s = DBShare()
    # l = s.get_list()

    # 分享拳的日期计算
    # import time,datetime
    # # print (time.strftime('%Y-%m-%d',time.localtime(time.time())))
    # today = datetime.date.today()
    # tomorrow = today + datetime.timedelta(days=1)
    # month_start = today.strftime('%Y-%m') + "-01"
    # db_share = DBShare()
    # c = db_share.count(store__uuid='d4c572a6-74ba-11e9-a56    5-e95aa2c51b5d',create_time__range=[today, tomorrow])

    # base64 编解码
    import base64
    import json
    encodestr = base64.b64decode('eyJtb2RlIjoiYXV0b19zaGFyZSIsInN0b3JlX3V1aWQiOiIzMjEiLCJzZWxsZXJfdXVpZCI6IjEyMyIsImRlYWRfdGltZSI6IjIwMTktNS0zMCJ9')
    print(encodestr)
    j = json.loads( str(encodestr,'utf-8'))
    print (j['mode'])
    # print (c)
    # print (l)