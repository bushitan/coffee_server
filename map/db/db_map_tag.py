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

    def get_index(self):
        _m = self.model.objects.filter(is_show = True).exclude(father = None)
        return self._pack_list( self._pack_dict,_m)

    def get_name_admin(self,tag_list):
        str = ''
        for tag in tag_list:
            str = str + tag.name_admin
            # list.append(tag.name_admin)
        return str

if __name__ == '__main__':
    import django
    django.setup()
    s = DBMapTag()
    l = s.get_list()
    tag = s.get(id=2)
    all = tag.tag_MapPOI.all()
    print (all)
    # .tag_mappoi.all()
    # print (poi)