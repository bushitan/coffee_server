#coding:utf-8
from lite.db.db import DB
from map.models import *


class DBMapTag(DB):
    def __init__(self):
        super().__init__(MapTag)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        _new = {
            "tag_id":object.id,
            "name":object.name,
            "name_admin":object.name_admin,
            "is_top":object.is_top,
            "service":object.service,
        }
        return dict(_base,**_new)

if __name__ == '__main__':
    s = DBMapTag()
    l = s.get_list()
    print (l)