#coding:utf-8
from lite.db.db import DBData
from lite.models import *


class DBPrize(DBData):
    def __init__(self):
        super().__init__(Prize)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        _new = {
        }
        return dict(_base,**_new)
if __name__ == '__main__':
    s = DBPrize()
    l = s.get_list()
    print (l)