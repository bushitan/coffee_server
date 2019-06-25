#coding:utf-8
from lite.db.db import DB
from map.db.db_map_tag import *
from map.models import *


class DBMapPOI(DB):
    def __init__(self):
        super().__init__(MapPOI)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        _new = {
            "id":object.id,
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

    # 根据tag获取poi
    def get_list_by_tag(self,tag_uuid):
        tag = MapTag.objects.get(uuid = tag_uuid)
        _m = tag.mappoi_set.filter(is_show = True) # 只查询要显示的点
        return self._pack_list( self._pack_dict,_m)

    # 获取poi的详情，获取相关文章
    def get_detail(self,poi_uuid):
        _m = self.model.objects.get(uuid=poi_uuid ,is_show = True)
        return self._pack_dict(_m)

    def get_detail_by_id(self,poi_id):
        _m = self.model.objects.get(id=poi_id ,is_show = True)
        return self._pack_dict(_m)


    def get_tag_name(self,obj):
        # _m = self.model.objects.get(uuid=poi_uuid)
        tag_list = obj.tag.all()
        db_tag = DBMapTag()
        return db_tag.get_name_admin( tag_list)


if __name__ == '__main__':
    import django
    django.setup()
    s = DBMapPOI()
    # print ( s.get_list_by_tag("e946a302-9241-11e9-93cb-e95aa2c51b5d") )
    # print ( s.get_detail("a17fc138-9243-11e9-9c7f-e95aa2c51b5d") )

    print (s.get_tag_name('a17fc138-9243-11e9-9c7f-e95aa2c51b5d'))

    # l = s.get_list()



    # print (l)