#coding:utf-8
from django.contrib import admin

from map.models import *
from lite.admin import *
from map.db.db_map_poi import *

# class LinkInline(admin.TabularInline):
# 	model = MapArticle
# 	min_num = 0
class MapPOIAdmin(BaseAdmin):
	list_display = ('id','store','name','tag_name','title','latitude','longitude','uuid',)
	fieldsets = (
        # (u"名称", {'fields': ['uuid','is_show','store',]}),
        (u"归属", {'fields': ['store','name','title','tag',]}),
		# (u"内容", {'fields': ['title']}),
		# (u"内容", {'fields': ['icon','title','summary','description',]}),
		(u"地址", {'fields': ['address','latitude','longitude',]}),
    )
	raw_id_fields = ("store",'icon',)
	list_filter = ('tag', )
	# inlines = [
	#     LinkInline,
	# ]

	def formfield_for_dbfield(self,db_field,**kwargs):
		if db_field.name == "tag":
			kwargs["queryset"] = MapTag.objects.all().exclude(father=None)
		return super().formfield_for_dbfield(db_field,**kwargs)
	filter_horizontal = ('tag',)

	# 展示tag的标签
	def tag_name(self,obj):
		db_poi = DBMapPOI()
		return db_poi.get_tag_name(obj)
	tag_name.short_description = u'所属分类'

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
	list_display = ('id','logo_image','nick_name','uuid','wx_openid',)
	fieldsets = (
        (u"客户属性", {'fields': ['type','uuid','name',]}),
		(u"微信数据", {'fields': ['logo_image','nick_name','avatar_url','gender','city','province','country',]}),
		(u"系统数据", {'fields': ['wx_openid','wx_session','wx_unionid',]}),
    )
	def logo_image(self, obj):
		return  mark_safe('<img src="%s" width="50px" />' % (obj.avatar_url))
	logo_image.short_description = u'图片'
	logo_image.allow_tags = True
	search_fields = ('id','wx_openid','uuid',)
	readonly_fields = ("uuid",'wx_openid','wx_session','wx_unionid','logo_image',)
admin.site.register(MapVisitor,MapVisitorAdmin)



class MapArticleAdmin(BaseAdmin):
	list_display = ('id','qr_image','author','poi','type','title','uuid',)
	# fieldsets = (
	#     (u"名称", {'fields': ['uuid','name','is_show',]}),
	#     (u"归属", {'fields': ['poi','type',]}),
	#     (u"作者", {'fields': ['author',]}),
		# (u"内容", {'classes': ('wide', 'extrapretty'),'fields': ['cover_image','cover','title','summary','description','content',]}),
		# (u"地址", {'fields': ['url','qr_image','qr',]}),
	# )
	fieldsets = (
		# (u"名称", {'fields': ['uuid','name','is_show',]}),
		(u"归属", {'fields': ['poi','type',]}),
		(u"作者", {'fields': ['author',]}),
		(u"小红书", {'fields': ['title','qr_image','qr',]}),
		(u"微信", {'fields': ['url',]}),
	)
	search_fields = ('poi__name',)
	list_filter = ('author', )
	raw_id_fields = ("poi",'cover','qr','author',)

	def cover_image(self, obj):
		if obj.cover is not None:
			return  mark_safe('<img src="%s" width="50px" />' % (obj.cover.url))
		else:
			return  mark_safe('<img src="" width="50px" />' )
	cover_image.short_description = u'封面'
	cover_image.allow_tags = True

	# 分享二维码的展示图片
	def qr_image(self, obj):
		if obj.qr is not None:
			return  mark_safe('<img src="%s?imageView2/1/w/96/h/96" name="%s" width="50px"  onclick="javascript:window.open(this.name)"/>' % (obj.qr.url,obj.qr.url))
		else:
			return  mark_safe('<img src="" width="50px" />' )
	qr_image.short_description = u'分享二维码'
	qr_image.allow_tags = True
	readonly_fields = ("cover_image","qr_image",)
admin.site.register(MapArticle,MapArticleAdmin)

