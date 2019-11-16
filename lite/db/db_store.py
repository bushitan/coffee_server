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

            "is_business":object.is_business,
            "is_ad":object.is_ad,

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


            "is_auto":object.is_auto,
            "mode":object.mode,
            "exchange_value":object.exchange_value,
            "check_value":object.check_value,
            "share_check_value":object.share_check_value,
            "share_num":object.share_num,
            "share_gift_value":object.share_gift_value,
            "share_limit_time":object.share_limit_time,
            "share_valid_time":object.share_valid_time,

            'icon_mode':object.icon_mode,
            'icon_check_image_url':object.icon_check_image_url,
            'icon_un_check_image_url':object.icon_un_check_image_url,
            'icon_full_image_url':object.icon_full_image_url,
            'icon_un_full_image_url':object.icon_un_full_image_url,
            'icon_ladder_cover_image_url':object.icon_ladder_cover_image_url,

            # 外卖模式
            "wm_mode":object.wm_mode,
            "wm_check_num":object.wm_check_num,
            "wm_share_num":object.wm_share_num,
        }
        return dict(_base,**_new)