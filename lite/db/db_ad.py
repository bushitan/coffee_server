#coding:utf-8
from lite.db.db import DB
from lite.models import *


class DBAd(DB):
    def __init__(self):
        super().__init__(Ad)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        _new = {
            "type":object.type,
            "cover":object.cover,
            "web_url":object.web_url,
            "sort":object.sort,
        }
        return dict(_base,**_new)

    def get_show_list(self):
        return self.get_list(is_show = True)


if __name__ == '__main__':
    import django
    django.setup()
    s = DBAd()
    l = s.get_show_list()
    print(l)

    # 分享拳的日期计算
    # import time,datetime
    # # print (time.strftime('%Y-%m-%d',time.localtime(time.time())))
    # today = datetime.date.today()
    # tomorrow = today + datetime.timedelta(days=1)
    # month_start = today.strftime('%Y-%m') + "-01"
    # db_share = DBShare()
    # c = db_share.count(store__uuid='d4c572a6-74ba-11e9-a56    5-e95aa2c51b5d',create_time__range=[today, tomorrow])

    # base64 编解码
    # import base64
    # import json
    # encodestr = base64.b64decode('eyJtb2RlIjoiYXV0b19zaGFyZSIsInN0b3JlX3V1aWQiOiIzMjEiLCJzZWxsZXJfdXVpZCI6IjEyMyIsImRlYWRfdGltZSI6IjIwMTktNS0zMCJ9')
    # print(encodestr)
    # j = json.loads( str(encodestr,'utf-8'))
    # print (j['mode'])
    # print (c)
    # print (l)