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
            "receive_customer_id":object.receive_customer_id,
            "receive_customer_avatar_url":object.receive_customer.avatar_url if object.receive_customer is not None else "" ,
            "receive_customer_nick_name":object.receive_customer.nick_name if object.receive_customer is not None else "" ,
            "receive_time":object.receive_time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        return dict(_base,**_new)
if __name__ == '__main__':
    s = DBShare()
    l = s.get_list()
    print (l)