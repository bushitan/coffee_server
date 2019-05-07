# -*- coding: utf-8 -*-
from django.contrib import admin
from lite.models import *

class BaseAdmin(admin.ModelAdmin):
	readonly_fields = ("uuid",)

from django.utils.safestring import mark_safe
class StoreAdmin(BaseAdmin):
	list_display = ('id','is_business','title','uuid','qr_image','mode','exchange_value','address','latitude','longitude',)

	fieldsets = (
		(u"展示内容", {'fields': ['is_business','uuid','title','summary','description','logo','icon','phone',]}),
		(u"分享内容", {'fields': ['share_logo','share_title',]}),
		(u"二维码", {'fields': ['qr_image','qr',]}),
		(u"地址", {'fields': ['address','latitude','longitude',]}),
		(u"核销兑换", {'fields': ['mode', 'exchange_value',]}),
		(u"普通模式", {'fields': ['check_value',]}),
		(u"分享模式", {'fields': [ 'share_check_value','share_gift_value',
                               'share_limit_time','share_valid_time', ]}),
    )
	search_fields = ('id','name',)
	def qr_image(self, obj):
		return  mark_safe('<img src="%s" width="100px" />' % (obj.qr))
	qr_image.short_description = u'店铺二维码'
	qr_image.allow_tags = True
	readonly_fields = ("uuid",'qr_image',)

admin.site.register(Store,StoreAdmin)


class SellerAdmin(BaseAdmin):
	list_display = ('id','store','is_host','nick_name','uuid','wx_openid',)
	fieldsets = (
        (u"销售属性", {'fields': ['store','is_host','uuid','name',]}),
		(u"微信数据", {'fields': ['nick_name','avatar_url','gender','city','province','country',]}),
		(u"系统数据", {'fields': ['wx_openid','wx_session','wx_unionid',]}),
    )
	search_fields = ('id','wx_openid','uuid',)
	readonly_fields = ("uuid",'wx_openid','wx_session','wx_unionid',)
admin.site.register(Seller,SellerAdmin)


class CustomerAdmin(BaseAdmin):
	list_display = ('id','name','nick_name','uuid','wx_openid',)
	fieldsets = (
        (u"客户属性", {'fields': ['uuid','name',]}),
		(u"微信数据", {'fields': ['nick_name','avatar_url','gender','city','province','country',]}),
		(u"系统数据", {'fields': ['wx_openid','wx_session','wx_unionid',]}),
    )
	search_fields = ('id','wx_openid','uuid',)
	readonly_fields = ("uuid",'wx_openid','wx_session','wx_unionid',)
admin.site.register(Customer,CustomerAdmin)


class RelStoreCustomerAdmin(BaseAdmin):
	list_display = ('id','store_id','customer_id','uuid','wx_openid',)
	fieldsets = (
        (u"关系", {'fields': ['store','customer',]}),
    )
	search_fields = ('id',)
admin.site.register(RelStoreCustomer,RelStoreCustomerAdmin)



class ScoreAdmin(BaseAdmin):
	list_display = ('id','is_used','store_id','seller_id','customer_id','exchange_time','share_id','is_delete',)
	fieldsets = (
        (u"公共数据", {'fields': ['is_used','exchange_time','share',]}),
        (u"集点数据", {'fields': ['store','seller','customer',]}),
        (u" 删除状态", {'fields': ['is_delete','delete_seller',]}),
        # (u"分享积分", {'fields': ['share',]}),
    )
	search_fields = ('id',)
admin.site.register(Score,ScoreAdmin)


class PrizeAdmin(BaseAdmin):
	list_display = ('id','store_id','seller_id','customer_id',)
	fieldsets = (
        (u"兑换", {'fields': ['store','customer','seller',]}),
    )
	search_fields = ('id',)
admin.site.register(Prize,PrizeAdmin)

class ShareAdmin(BaseAdmin):
	list_display = ('id','store_id','uuid','seller_id','customer_id','receive_customer','valid_time','create_time',)
	fieldsets = (
        (u"兑换", {'fields': ['uuid','store','seller','customer','receive_customer','receive_time','valid_time','create_time',]}),
    )
	search_fields = ('id',)
admin.site.register(Share,ShareAdmin)