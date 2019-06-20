#coding:utf-8
from django.db import models
from lite.models import *
from lib.util import *
class MapPOI(Base):
    store = models.ForeignKey(Store, verbose_name=u'所属店铺',null=True,blank=True)
    tag = models.ManyToManyField('MapTag', verbose_name=u'标签',null=True,blank=True)

    icon = models.ForeignKey(BaseImage, verbose_name=u'封面图片',null=True,blank=True)
    title = models.CharField(max_length=100, verbose_name=u'标题',default="",null=True,blank=True)
    summary = models.CharField(max_length=200, verbose_name=u'简介',default="",null=True,blank=True)
    description = models.CharField(max_length=500, verbose_name=u'描述',default="",null=True,blank=True)

    # navigate = models.TextField(verbose_name=u'实景导航',null=True,blank=True)
    address = models.CharField(max_length=100, verbose_name=u'地址',default="",null=True,blank=True)
    latitude =  models.FloatField( verbose_name=u'纬度',default=0,null=True,blank=True)
    longitude =  models.FloatField(  verbose_name=u'经度',default=0,null=True,blank=True)

    is_show = models.BooleanField(u'是否展示',default=True)
    class Meta:
        verbose_name_plural = verbose_name = u'POI地址'
    def __str__(self):
        return '%s' % (self.title )

class MapTag(Base):
    name_admin = models.CharField(max_length=32, verbose_name=u'后台显示名字',default="",null=True,blank=True)
    father = models.ForeignKey('self', verbose_name=u'父类',null=True,blank=True)
    sort = models.IntegerField(u'排序',default=0)
    is_top = models.BooleanField(u'是否置顶',default=False)
    service = models.IntegerField(u'服务状态',default=STORE_MODE_NORMAL,choices=STORE_MODE.items())
    is_show = models.BooleanField(u'是否展示',default=True)
    class Meta:
        verbose_name_plural = verbose_name = u'标签'
    def __str__(self):
        return '%s' % (self.name )


# 客户
class MapVisitor(User):
    type = models.IntegerField(u'类别',default=MAP_VISITOR_TYPE_NORMAL,choices=MAP_VISITOR_TYPE.items())
    class Meta:
        verbose_name_plural = verbose_name = u'浏览者'
    def __str__(self):
        return '%s' % (self.nick_name)



# 客户
class MapArticle(Base):
    poi = models.ForeignKey(MapPOI, verbose_name=u'所属POI点',null=True,blank=True)
    type = models.IntegerField(u'类别',default=MAP_ARTICLE_TYPE_WX,choices=MAP_ARTICLE_TYPE.items())

    author = models.ForeignKey(MapVisitor, verbose_name=u'博主',null=True,blank=True)

    cover = models.ForeignKey(BaseImage, verbose_name=u'封面图片',related_name='cover',null=True,blank=True)
    title = models.CharField(max_length=100, verbose_name=u'标题',default="",null=True,blank=True)
    summary = models.CharField(max_length=200, verbose_name=u'简介',default="",null=True,blank=True)
    description = models.CharField(max_length=500, verbose_name=u'描述',default="",null=True,blank=True)
    content = models.TextField(verbose_name=u'内容',null=True,blank=True)
    url = models.CharField(max_length=1000, verbose_name=u'web地址',null=True,blank=True)
    qr = models.ForeignKey(BaseImage, verbose_name=u'二维码',related_name='qr',null=True,blank=True)

    is_show = models.BooleanField(u'是否展示',default=True)
    class Meta:
        verbose_name_plural = verbose_name = u'文章'
    def __str__(self):
        return '%s' % (self.title)



# 序号	名称	英文	属性	备注
# 1	公共	base	name
# 2			uuid
# 3			short_uuid
# 4			create_time
# 5	地址	map_poi	store	内容
# 6			tag
# 7			logo
# 8			title
# 9			summary
# 10			content
# 11			navigate	地址
# 12			address
# 13			latitude
# 14			longitude
# 15			share_logo	分享
# 16			share_title
# 17	用户	map_visitor	User	继承
# 18	内容	map_article	map_poi
# 19			type	类型：小红书，公众号、马蜂窝
# 20			title
# 21			summary
# 22			content
# 23			url
# 24			qr_image	image图片对象
# 25
# 26	标签	map_tag	name_admin	admin显示的米棒子
# 27			father	父类
# 28			sort	排序，由高到低
# 29			is_top	置顶
# 30			status	服务状态
# 图片	image	type	类型：cover，qr,icon
#