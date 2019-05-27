#coding:utf-8
from lite.db.db import DB
from lite.models import *


class DBStore(DB):
    def __init__(self):
        super(DBStore,self).__init__(Store)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        _new = {
            "title":object.title,
            "summary":object.summary,
            "description":object.description,
            "logo":object.logo,
            "icon":object.icon,
            "phone":object.phone,
            "start_time":object.start_time.strftime("%Y-%m-%d"),
            "end_time":object.end_time.strftime("%Y-%m-%d"),

            "share_logo":object.share_logo,
            "share_title":object.share_title,

            "address":object.address,
            "latitude":object.latitude,
            "longitude":object.longitude,


            "mode":object.mode,
            "exchange_value":object.exchange_value,
            "check_value":object.check_value,
            "share_check_value":object.share_check_value,
            "share_num":object.share_num,
            "share_gift_value":object.share_gift_value,
            "share_limit_time":object.share_limit_time,
            "share_valid_time":object.share_valid_time,
        }
        return dict(_base,**_new)