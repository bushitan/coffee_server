#coding:utf-8
from django.conf.urls import url
from .views import  *

urlpatterns = [
    url(r'^index/',MapIndex.as_view()),
    url(r'^search/poi/list/',MapGetPOIList.as_view()),
    url(r'^search/poi/detail/',MapGetPOIDetail.as_view()),
    url(r'^search/article/detail/',MapGetArticle.as_view()),

    url(r'^search/poi/store/',MapGetPOIByStore.as_view()),
]
