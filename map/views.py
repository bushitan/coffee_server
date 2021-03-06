#coding:utf-8
from django.views.generic import ListView
from lib.logged import logged
import lite.uitls.message as MSG
import lite.uitls.detection as det

from map.action.action_search import *
action_search = ActionSearch()

# @地图初始化
class MapIndex(ListView):
    @logged
    def post(self, request, *args, **kwargs):
        # tag_list = action_search.get_tag()
        # poi_list = action_search.get_poi_by_tag(tag_list[0]['uuid'])
        _dict = {
            'drink_list':action_search.get_poi_by_tag('be62eade-9566-11e9-940a-e95aa2c51b5d'),
            'eat_list':action_search.get_poi_by_tag('e946a302-9241-11e9-93cb-e95aa2c51b5d'),
            'play_list':action_search.get_poi_by_tag('c275b3ae-9566-11e9-8016-e95aa2c51b5d'),
        }
        return MSG.sys_success(), _dict

# @地图初始化
class MapGetPOIList(ListView):
    @logged
    def post(self, request, *args, **kwargs):
        tag_uuid = request.POST.get('tag_uuid','')
        poi_list = action_search.get_poi_by_tag(tag_uuid)
        _dict = {
            'poi_list':poi_list,
        }
        return MSG.sys_success(), _dict



# 查询poi点信息
class MapGetPOIDetail(ListView):
    @logged
    def post(self, request, *args, **kwargs):
        poi_id = request.POST.get('poi_id','')
        poi_dict = action_search.get_poi_by_id(poi_id)
        article_list = action_search.get_article_list_by_poi(poi_id)
        _dict = {
            'poi_dict':poi_dict,
            'article_list':article_list,
        }
        return MSG.sys_success(), _dict
        #
        #

# 查询poi点信息
class MapGetArticle(ListView):
    @logged
    def post(self, request, *args, **kwargs):
        article_uuid = request.POST.get('article_uuid','')
        article_dict = action_search.get_article(article_uuid)
        _dict = {
            'article_dict':article_dict,
        }
        return MSG.sys_success(), _dict




'''
    @method
        根据店铺uuid，获取poi列表
    @param
        store_uuid 店铺uuid
    @return
        poi_list poi列表
'''
class MapGetPOIByStore(ListView):
    @logged
    def post(self, request, *args, **kwargs):
        store_id = request.POST.get('store_id','')
        _dict = {
            'poi_list':action_search.get_poi_by_store(store_id = store_id),
        }
        return MSG.sys_success(), _dict