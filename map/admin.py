#coding:utf-8
from django.contrib import admin

from map.models import *
from lite.admin import *


class MapPOIAdmin(BaseAdmin):
	list_display = ('id','store','title','latitude','longitude',)
	fieldsets = (
        (u"名称", {'fields': ['uuid','name','is_show',]}),
        (u"归属", {'fields': ['store','tag',]}),
		(u"内容", {'fields': ['icon','title','summary','description',]}),
		(u"地址", {'fields': ['address','latitude','longitude',]}),
    )
	raw_id_fields = ("store",'icon',)

	def formfield_for_dbfield(self,db_field,**kwargs):
		if db_field.name == "tag":
			kwargs["queryset"] = MapTag.objects.all().exclude(father=None)
		return super().formfield_for_dbfield(db_field,**kwargs)

	filter_horizontal = ('tag',)
	# search_fields = ('id','wx_openid','uuid','nick_name','store__title',)
	# readonly_fields = ("uuid",'wx_openid','wx_session','wx_unionid',)
admin.site.register(MapPOI,MapPOIAdmin)



class MapTagAdmin(BaseAdmin):
	list_display = ('id','name_admin','name','father','service','is_top','sort',)
	fieldsets = (
        (u"名称", {'fields': ['uuid','name','name_admin','is_show',]}),
        (u"归属", {'fields': ['father','service',]}),
		(u"内容", {'fields': ['is_top','service','sort',]}),
    )
	raw_id_fields = ("father",)
admin.site.register(MapTag,MapTagAdmin)


class MapVisitorAdmin(BaseAdmin):
	list_display = ('id','name','nick_name','uuid','wx_openid',)
	fieldsets = (
        (u"客户属性", {'fields': ['uuid','name',]}),
		(u"微信数据", {'fields': ['nick_name','avatar_url','gender','city','province','country',]}),
		(u"系统数据", {'fields': ['wx_openid','wx_session','wx_unionid',]}),
    )
	search_fields = ('id','wx_openid','uuid',)
	readonly_fields = ("uuid",'wx_openid','wx_session','wx_unionid',)
admin.site.register(MapVisitor,MapVisitorAdmin)



class MapArticleAdmin(BaseAdmin):
	list_display = ('id','poi','type','title',)
	fieldsets = (
        (u"名称", {'fields': ['uuid','name','is_show',]}),
        (u"归属", {'fields': ['poi','type',]}),
		(u"内容", {'fields': ['cover','title','summary','description','content',]}),
		(u"地址", {'fields': ['url','qr',]}),
    )
	raw_id_fields = ("poi",'cover','qr',)

			# kwargs["queryset"]=User.objects.filter(profile_user__pid=self.user.id)
	# search_fields = ('id','wx_openid','uuid','store__title',)
	# readonly_fields = ("uuid",'wx_openid','wx_session','wx_unionid',)
admin.site.register(MapArticle,MapArticleAdmin)

