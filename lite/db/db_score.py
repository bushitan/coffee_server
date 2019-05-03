#coding:utf-8
from lite.db.db import DBData
from lite.models import *


class DBScore(DBData):
    def __init__(self):
        super().__init__(Score)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        _new = {
            "is_used":object.is_used,
            "exchange_time":object.exchange_time.strftime("%Y-%m-%d %H:%M:%S"),
            "share_id":object.share_id,
        }
        return dict(_base,**_new)
if __name__ == '__main__':
    import django
    django.setup()
    s = DBScore()
    query = { 'store_': 1}
    l =  s.get_list(**query )
    print (l)