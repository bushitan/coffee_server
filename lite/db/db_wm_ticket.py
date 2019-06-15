#coding:utf-8
from lite.db.db import DB
from lite.models import *


class DBWmTicket(DB):
    def __init__(self):
        super().__init__(WmTicket)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        _new = {
            "store_id":object.store_id,
            "share_id":object.share_id,
            "score_id":object.score_id,
            "customer_id":object.customer_id,
            "is_used":object.is_used,
            "is_delete":object.is_delete,
            "start_time":object.start_time,
            "end_time":object.end_time,
        }
        return dict(_base,**_new)

if __name__  == '__main__':
    import django
    django.setup()
    a= DBWmTicket()
    # a.get_dict(uuid = '	957a6946-63f8-11e9-8597-b83312f00bac')
    # print (a.get_dict(id = 1 ))
    # print (a.get_dict(uuid = '957a6946-63f8-11e9-8597-b83312f00bac' ))
    # print (a.update( a.filter(id=3),store_id = 1 ))