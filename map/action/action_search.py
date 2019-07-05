#coding:utf-8

from django.db import transaction
from map.db.db_map_poi import *
from map.db.db_map_tag import *
from map.db.db_map_article import *
from lite.db.db_store import *
from lib.util import *
import time
import datetime
class ActionSearch():
    def __init__(self):
        self.db_map_poi = DBMapPOI()
        self.db_map_tag = DBMapTag()
        self.db_map_article = DBMapArticle()
        self.db_store = DBStore()

    # 获取要展示的标签
    def get_tag(self):
         return self.db_map_tag.get_index()

    # 获取tag下的poi点位
    def get_poi_by_tag(self,tag_uuid):
         return self.db_map_poi.get_list_by_tag(tag_uuid)

    # 获取单个poi点位
    def get_poi(self,poi_uuid):
         return self.db_map_poi.get_detail(poi_uuid)
    # 获取单个poi点位
    def get_poi_by_id(self,poi_id):
         return self.db_map_poi.get_detail_by_id(poi_id)

    # POI点，获取文章列表
    def get_article_list_by_poi(self,poi_id):
        return self.db_map_article.get_list_by_poi(poi_id)

    # 获取文章内容
    def get_article(self,article_uuid):
        return self.db_map_article.get_dict(uuid=article_uuid)


    '''
        @method
            获取店铺的poi列表
        @param
            store_uuid 店铺uuid
        @return
            poi_list poi点
    '''
    def get_poi_by_store(self,store_id):
        store = self.db_store.get(id = store_id) # 店铺对象
        print (store)
        return self.db_map_poi.get_list(store = store) # poi列表


if __name__  == '__main__':
    import django
    django.setup()
    acs = ActionSearch()
    # print (acs.get_article( '58aac768-9262-11e9-bb1d-e95aa2c51b5d'))
    poi_list = acs.get_poi_by_store(store_uuid = "54931e42-7c67-11e9-b94e-e95aa2c51b5d")
    print (poi_list)













