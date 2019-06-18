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
        }
        return dict(_base,**_new)

if __name__ == '__main__':
    s = DBMapArticle()
    l = s.get_list()
    print (l)