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
        tag_list = action_search.get_tag()
        poi_list = action_search.get_poi_by_tag(tag_list[0]['uuid'])
        _dict = {
            'tag_list':tag_list,
            'poi_list':poi_list,
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
        poi_uuid = request.POST.get('poi_uuid','')
        poi_dict = action_search.get_poi(poi_uuid)
        article_list = action_search.get_article_list_by_poi(poi_uuid)
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

