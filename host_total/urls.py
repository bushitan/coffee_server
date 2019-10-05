#coding:utf-8
from django.conf.urls import url
from .views import  *

urlpatterns = [

    # url(r'^error/test/',ErrorTest.as_view()),

    # 公共
    url(r'^login/',UserLogin.as_view()),
    url(r'^check/',UserLoginCheck.as_view()),
    url(r'^total/',Total.as_view()),
    url(r'^map/',ScoreMap.as_view()),
    url(r'^seller/list/',SellerList.as_view()),
    url(r'^seller/detail/',SellerDetail.as_view()),
]
