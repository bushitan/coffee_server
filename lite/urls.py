#coding:utf-8
from django.conf.urls import url
from .views import  *

urlpatterns = [
    # 公共
    url(r'^route/user/login/',UserLogin.as_view()),
    url(r'^route/user/update/',UserUpdate.as_view()),
    url(r'^store/info/',StoreInfo.as_view()),

    # 客户
    url(r'^store/list/customer/',CustomerStore.as_view()),
    url(r'^store/data/customer/',CustomerData.as_view()),
    url(r'^store/detail/customer/',CustomerDetail.as_view()),
    url(r'^store/share/customer/',CustomerShare.as_view()),
    url(r'^refresh/customer',CustomerRefresh.as_view()),

    url(r'^scan/auto_share/customer/',CustomerScanAutoShare.as_view()),
    url(r'^scan/wm/customer/',CustomerScanWm.as_view()), #客户扫码，自助模式
    url(r'^scan/wm/check/customer/',CustomerScanWmCheck.as_view()),

    # 商户
    url(r'^store/update/seller/',SellerUpdate.as_view()),
    url(r'^store/data/seller/',SellerData.as_view()),
    url(r'^store/host/data/seller/',SellerHostData.as_view()),
    url(r'^store/auto_share/qr/seller/',SellerAutoShareQR.as_view()),  #获取自助二维码

    url(r'^share/delete/seller/',SellerShareDelete.as_view()),

    url(r'^scan/seller/',SellerScan.as_view()),
    url(r'^scan/score/seller/',SellerScanScore.as_view()),
    url(r'^scan/share/seller/',SellerScanShare.as_view()),
    url(r'^scan/prize/seller/',SellerScanPrize.as_view()),

    # url(r'^scan/info/',SellerScanPrize.as_view()),

 # url(r'^store/invite/seller/',SellerInvite.as_view()),
 #    url(r'^store/quit/seller/',SellerQuit.as_view()),
    # url(r'^store/apply/seller/',SellerApply.as_view()), # 暂无
    # url(r'^store/dissolve/seller/',Index55.as_view()),
]
