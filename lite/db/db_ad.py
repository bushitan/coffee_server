#coding:utf-8
from lite.db.db import DB
from lite.models import *


class DBAd(DB):
    def __init__(self):
        super().__init__(Ad)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        _new = {
            "id":object.id,
            "type":object.type,
            "cover_image_url":object.cover_image.url if object.cover_image is not None else "" ,
            "content_image_url":object.content_image.url if object.content_image is not None else "" ,
            'content_url':object.content_url,
            'content_lite_app_id':object.content_lite_app_id,
            'content_lite_path':object.content_lite_path,
            'content_lite_extra_data':object.content_lite_extra_data,
            'content_lite_env_version':object.content_lite_env_version,
            "cover":object.cover,
            "web_url":object.web_url,
            "sort":object.sort,
        }
        return dict(_base,**_new)

    '''
        @method 获取能展示的所有广告
    '''
    def get_show_list(self):
        return self.get_list(is_show = True)

    '''
        @method 获取店铺能展示的广告
    '''
    def get_store_list(self,store_uuid):
        q = self.model.objects.filter(Q(is_show = True) &  Q( Q(store__uuid = store_uuid) | Q(store__uuid = None)))
        return self._pack_list(self._pack_dict,q)
        # return self.get_list(is_show = True)


if __name__ == '__main__':
    import django
    django.setup()
    s = DBAd()
    # l = s.get_show_list()
    # print(l)
    store_uuid = '68e54718-7156-11e9-b456-e95aa2c51b5d'
    # store_uuid ='a5e75dae-7158-11e9-84b7-e95aa2c51b5d'
    store_ad_list = s.get_store_list(store_uuid)
    print(store_ad_list)

    # 分享拳的日期计算
    # import time,datetime
    # # print (time.strftime('%Y-%m-%d',time.localtime(time.time())))
    # today = datetime.date.today()
    # tomorrow = today + datetime.timedelta(days=1)
    # month_start = today.strftime('%Y-%m') + "-01"
    # db_share = DBShare()
    # c = db_share.count(store__uuid='d4c572a6-74ba-11e9-a56    5-e95aa2c51b5d',create_time__range=[today, tomorrow])

    # base64 编解码
    # import base64
    # import json
    # encodestr = base64.b64decode('eyJtb2RlIjoiYXV0b19zaGFyZSIsInN0b3JlX3V1aWQiOiIzMjEiLCJzZWxsZXJfdXVpZCI6IjEyMyIsImRlYWRfdGltZSI6IjIwMTktNS0zMCJ9')
    # print(encodestr)
    # j = json.loads( str(encodestr,'utf-8'))
    # print (j['mode'])
    # print (c)
    # print (l)