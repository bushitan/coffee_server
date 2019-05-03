#coding:utf-8
from lite.db.db import DBUser
from lite.models import *


class DBCustomer(DBUser):
    def __init__(self):
        super().__init__(Customer)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        _new = {
        }
        return dict(_base,**_new)

if __name__  == '__main__':
    a= DBCustomer()
    # a.get(uuid = '67e3f912-63d4-11e9-9b5d-b83312f00bac')