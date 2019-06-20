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
         return self.db_map_tag.get_index()

    # 获取tag下的poi点位
    def get_poi_by_tag(self,tag_uuid):
         return self.db_map_poi.get_list_by_tag(tag_uuid)

    # 获取单个poi点位
    def get_poi(self,poi_uuid):
         return self.db_map_poi.get_detail(poi_uuid)

    # POI点，获取文章列表
    def get_article_list_by_poi(self,poi_uuid):
        return self.db_map_article.get_list_by_poi(poi_uuid)

    # 获取文章内容
    def get_article(self,article_uuid):
        return self.db_map_article.get_dict(uuid=article_uuid)

if __name__  == '__main__':
    import django
    django.setup()
    acs = ActionSearch()
    print (acs.get_article( '58aac768-9262-11e9-bb1d-e95aa2c51b5d'))














