#coding:utf-8
from lite.db.db import DB
from map.models import *


class DBMapPOI(DB):
    def __init__(self):
        super().__init__(MapPOI)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        _new = {
            "store_id":object.store_id,

            "icon":object.icon.url if object.icon is not None else "" ,
            "title":object.title,
            "summary":object.summary,
            "description":object.description,

            "address":object.address,
            "latitude":object.latitude,
            "longitude":object.longitude,
        }
        return dict(_base,**_new)

if __name__ == '__main__':
    s = DBMapPOI()
    l = s.get_list()
    print (l)