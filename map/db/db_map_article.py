#coding:utf-8
from lite.db.db import DB
from map.models import *


class DBMapArticle(DB):
    def __init__(self):
        super().__init__(MapArticle)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        _new = {
            "poi_id":object.poi_id,
            "type":object.type,

            "cover":object.cover.url if object.cover is not None else "" ,
            "title":object.title,
            "summary":object.summary,
            "description":object.description,
            "content":object.content,

            "url":object.url,
            "qr":object.qr.url if object.qr is not None else "" ,


            "author_nick_name":object.author.nick_name if object.author is not None else "" ,
            "author_avatar_url":object.author.avatar_url if object.author is not None else "" ,
        }
        return dict(_base,**_new)

    # 获取poi的详情，获取相关文章
    def get_list_by_poi(self,poi_id):
        _m = self.model.objects.filter(poi_id=poi_id, is_show = True)
        return self._pack_list( self._pack_dict,_m)


if __name__ == '__main__':
    import django
    django.setup()
    s = DBMapArticle()
    print(s.get_list_by_poi('a17fc138-9243-11e9-9c7f-e95aa2c51b5d'))
    # l = s.get_list()
    # print (l)