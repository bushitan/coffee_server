#coding:utf-8

from django.db import transaction
from map.db.db_map_poi import *
from map.db.db_map_tag import *
from map.db.db_map_article import *
from lib.util import *
import time
import datetime
class ActionSearch():
    def __init__(self):
        self.db_map_poi = DBMapPOI()
        self.db_map_tag = DBMapTag()
        self.db_map_article = DBMapArticle()

    # 获取要展示的标签
    def get_tag(self):
         return self.db_map_tag.get_list(is_show = True)

    # 获取tag下的poi点位
    def get_poi_by_tag(self,tag_uuid):
         return self.db_map_poi.get_list(tag__uuid=tag_uuid ,is_show = True)

    # 获取poi点位
    def get_poi(self,poi_uuid):
         return self.db_map_poi.get_dict(uuid=poi_uuid ,is_show = True)

    # POI点，获取文章列表
    def get_article_by_poi(self,poi_uuid):
        return self.db_map_article.get_list(poi__uuid=poi_uuid, is_show = True)

    # 获取文章内容
    def get_article(self,article_uuid):
        return self.db_map_article.get_dict(id=article_uuid)

if __name__  == '__main__':
    wm = ActionSearch()
       # 3smX46fZ
    # wm.check_score(
    #     wm_short_uuid='3smX46fZ',
    #     customer_uuid="1eeabca4-7156-11e9-ad02-e95aa2c51b5d"
    # )
    wm.check_share(
        wm_short_uuid='3smX46fZ',
        customer_uuid="1eeabca4-7156-11e9-ad02-e95aa2c51b5d"
    )


        # share_valid_time = store.share_valid_time
        # share_num = store.share_num
        # now = datetime.datetime.now()
        # now_stamp = time.mktime(now.timetuple())
        # valid = now_stamp + share_valid_time * UNIT_SECOND
        # valid_time = datetime.datetime.fromtimestamp(valid)














