#coding:utf-8
from django.db import models
from lib.util import *
import django.utils.timezone as timezone
def day_365_hence(): #集点默认365天有效期
    return timezone.now() + timezone.timedelta(days=365)

import uuid
import pymysql
pymysql.install_as_MySQLdb()

from lib.image_utils import *

from lib.short_uuid import short_uuid_create

# 基础类 虚函数
class Base(models.Model):
    name = models.CharField(max_length=32, verbose_name=u'名字',default="",null=True,blank=True)
    uuid = models.CharField(max_length=36, verbose_name=u'uuid',default="",null=True,blank=True)
    short_uuid = models.CharField(max_length=36, verbose_name=u'短uuid',default="",null=True,blank=True)
    create_time = models.DateTimeField(u'创建时间',default = timezone.now)
    class Meta:
        abstract = True
    def save(self, *args, **kwargs):
            # 创建用户时，生成唯一ID
            print (self)
            if not self.uuid:
                self.uuid = str( uuid.uuid1())
            if not self.short_uuid:
                self.short_uuid = short_uuid_create(self.uuid)
            super(Base,self).save(*args, **kwargs)

# 图片库
class BaseImage(Base):
    url = models.CharField(max_length=1000, verbose_name=u'云地址',null=True,blank=True)
    local_path = models.ImageField(u'图标',upload_to=ImageUtils.rename,null=True,blank=True)
    type = models.IntegerField(u'类别',default=BASE_IMAGE_TYPE_QR,choices=BASE_IMAGE_TYPE.items())
    class Meta:
        verbose_name_plural = verbose_name = u'图库'
    def __unicode__(self):
        return '%s' % (self.id)
    def save(self):
        super().save()
        if not self.url:
            self.url = QINIU_HOST + self.local_path.url
        key = self.local_path.url
        local_file = MEDIA_ROOT+key
        ImageUtils.put(key,local_file)
        super().save()
        # image_utils = ImageUtils()
        # # image_utils.rename()
        # print (self.local_path)


# 店铺
class Store(Base):
    is_business = models.BooleanField(u'是否营业',default=True)
    title = models.CharField(max_length=100, verbose_name=u'标题',default="",null=True,blank=True)
    summary = models.CharField(max_length=200, verbose_name=u'简介',default="",null=True,blank=True)
    description = models.CharField(max_length=500, verbose_name=u'描述',default="",null=True,blank=True)
    logo = models.CharField(max_length=500, verbose_name=u'LOGO',default="",null=True,blank=True)
    share_logo = models.CharField(max_length=500, verbose_name=u'分享LOGO',default="",null=True,blank=True)
    share_title = models.CharField(max_length=100, verbose_name=u'分享标题',default="",null=True,blank=True)
    icon = models.CharField(max_length=500, verbose_name=u'图标',default="",null=True,blank=True)
    phone =  models.CharField(max_length=32, verbose_name=u'电话',default="",null=True,blank=True)

    qr =  models.TextField(verbose_name=u'店铺二维码',default="",null=True,blank=True)

    address = models.CharField(max_length=100, verbose_name=u'地址',default="",null=True,blank=True)
    latitude =  models.FloatField( verbose_name=u'纬度',default=0,null=True,blank=True)
    longitude =  models.FloatField(  verbose_name=u'经度',default=0,null=True,blank=True)

    is_auto = models.BooleanField(u'是否自助集点',default=False)
    mode = models.IntegerField(u'集点模式',default=STORE_MODE_NORMAL,choices=STORE_MODE.items())
    exchange_value = models.IntegerField(u'兑换礼物点数',default=10)
    check_value = models.IntegerField(u'普通核销点数',default=1)
    share_check_value = models.IntegerField(u'分享券核销点数',default=1)
    share_gift_value = models.IntegerField(u'分享券获赠点数',default=1)
    share_num = models.IntegerField(u'分享人数',default=1)
    share_limit_time = models.IntegerField(u'分享券领取时间间隔(天）',default=1)
    share_valid_time = models.IntegerField(u'分享券有效期(天）',default=1)

    icon_mode = models.IntegerField(u'图标模式',default=STORE_ICON_MODE_CUP,choices=STORE_ICON_MODE.items())
    icon_check_image_url = models.CharField(max_length=500, verbose_name=u'已集点印章图标',default="",null=True,blank=True)
    icon_un_check_image_url = models.CharField(max_length=500, verbose_name=u'未集点印章图标',default="",null=True,blank=True)
    icon_full_image_url = models.CharField(max_length=500, verbose_name=u'集满点印章图标',default="",null=True,blank=True)
    icon_un_full_image_url = models.CharField(max_length=500, verbose_name=u'未集满点印章图标',default="",null=True,blank=True)

    wm_mode = models.IntegerField(u'外卖模式',default=STORE_WM_MODE_NORMAL,choices=STORE_WM_MODE.items())
    wm_check_num =  models.IntegerField(u'发放普通核销点数量',default=1)
    wm_share_num =  models.IntegerField(u'发放分享券数量',default=1)

    start_time = models.DateTimeField(u'集点开始时间',default = timezone.now)
    end_time = models.DateTimeField(u'集点结束时间',default = day_365_hence)

    class Meta:
        verbose_name_plural = verbose_name = u'商铺'
    def __str__(self):

        return '%s' % (self.title )















# 用户 虚函数
class User(Base):
    nick_name =  models.CharField(max_length=100, verbose_name=u'昵称',default="",null=True,blank=True)
    avatar_url =  models.CharField(max_length=500, verbose_name=u'头像',default="",null=True,blank=True)
    gender =  models.CharField(max_length=100, verbose_name=u'性别',default="",null=True,blank=True)
    city =  models.CharField(max_length=100, verbose_name=u'城市',default="",null=True,blank=True)
    province =  models.CharField(max_length=100, verbose_name=u'省份',default="",null=True,blank=True)
    country =  models.CharField(max_length=100, verbose_name=u'国家',default="",null=True,blank=True)
    # login
    wx_openid = models.CharField(max_length=50, verbose_name=u'微信OpenID',default="",null=True,blank=True)
    wx_session = models.CharField( max_length=128,verbose_name=u'微信SessionKey',default="",null=True,blank=True)
    wx_unionid = models.CharField(max_length=50, verbose_name=u'微信UnionID',default="",null=True,blank=True)
    class Meta:
        abstract = True


# 店家
class Seller(User):
    is_host= models.BooleanField(u'是否店主',default=False)
    store = models.ForeignKey(Store, verbose_name=u'所属店铺',null=True,blank=True)

    class Meta:
        verbose_name_plural = verbose_name = u'店家'
    def __str__(self):
        return '%s' % (self.nick_name)

# 客户
class Customer(User):
    class Meta:
        verbose_name_plural = verbose_name = u'客户'
    def __str__(self):
        return '%s' % (self.nick_name)

# 客户访问的店铺表
class RelStoreCustomer(User):
    store = models.ForeignKey(Store,verbose_name=u'所属店铺',null=True,blank=True)
    customer = models.ForeignKey(Customer,verbose_name=u'所属店铺',null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'客户访问的店铺表'
    def __unicode__(self):
        return '%s' % (self.id)




























# SCORE_MODE =  {
# 	STORE_MODE_NORMAL:u"普通模式",
# 	STORE_MODE_SHARE:u"分享模式",
# }
# 用户 虚函数
class DataBase(Base):
    store = models.ForeignKey(Store,verbose_name=u'所属店铺',null=True,blank=True)
    seller = models.ForeignKey(Seller, verbose_name=u'核销店员',null=True,blank=True)
    customer = models.ForeignKey(Customer,verbose_name=u'所属客户',null=True,blank=True)
    valid_time = models.DateTimeField(u'有效期',default = timezone.now)
    is_delete = models.BooleanField(u'是否被删除',default=False)
    # source = models.IntegerField(u'来源（默认扫码）',default=DATA_SOURCE_SCAN,choices=DATA_SOURCE.items())
    class Meta:
        abstract = True
# 积分
class Score(DataBase):
    is_used= models.BooleanField(u'是否已使用',default=False)
    exchange_time = models.DateTimeField(u'礼物兑换时间',default = timezone.now)
    share = models.ForeignKey('Share', verbose_name=u'分享券',null=True,blank=True)
    wm_ticket = models.ForeignKey('WmTicket', verbose_name=u'外卖码',null=True,blank=True)

    # is_delete = models.BooleanField(u'是否被删除',default=False)
    delete_seller = models.ForeignKey(Seller, related_name='score_delete_seller',verbose_name=u'删除的店员',null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'积分'
        ordering = ['-create_time']
    def __str__(self):
        return '%s' % (self.id)

# 分享券
class Share(DataBase):
    receive_customer = models.ForeignKey(Customer,related_name='receive_customer', verbose_name=u'接受客户',null=True,blank=True)
    receive_time = models.DateTimeField(u'接受时间',default = timezone.now)
    alive = models.IntegerField(u'有效份数',default=1)
    delete_seller = models.ForeignKey(Seller, related_name='share_delete_seller',verbose_name=u'删除的店员',null=True,blank=True)
    wm_ticket = models.ForeignKey('WmTicket', verbose_name=u'外卖码',null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'分享券'
        ordering = ['-create_time']
    def __str__(self):
        return '%s' % (self.id)

# 奖品
class Prize(DataBase):
    delete_seller = models.ForeignKey(Seller, related_name='prize_delete_seller',verbose_name=u'删除的店员',null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'奖品'
        ordering = ['-create_time']
    def __str__(self):
        return '%s' % (self.id)



class WmTicket(Base):
    store = models.ForeignKey(Store,verbose_name=u'所属店铺',null=True,blank=True)
    customer = models.ForeignKey(Customer,verbose_name=u'领取客户',null=True,blank=True)
    is_used= models.BooleanField(u'是否已使用',default=False)
    is_delete = models.BooleanField(u'是否被删除',default=False)
    start_time = models.DateTimeField(u'外卖活动开始时间',default = timezone.now)
    end_time = models.DateTimeField(u'外卖活动结束时间',default = day_365_hence)
    class Meta:
        verbose_name_plural = verbose_name = u'外卖二维码'
        ordering = ['-create_time']
    def __str__(self):
        return '%s' % (self.id)




# class Shop(BaseModel):
# 	name =  models.CharField(max_length=32, verbose_name=u'店铺名称',default="",null=True,blank=True)
# 	# poi =  models.ForeignKey( POI,verbose_name=u'对应poi点')
# 	group =  models.ForeignKey( Group,verbose_name=u'所属group群组',null=True,blank=True)
# 	user =  models.ForeignKey( User,verbose_name=u'所属用户',null=True,blank=True)
# 	title =  models.CharField(max_length=32, verbose_name=u'标题',default="",null=True,blank=True)
# 	summary =  models.CharField(max_length=32, verbose_name=u'简介',default="",null=True,blank=True)
# 	logo =  models.CharField(max_length=500, verbose_name=u'logo',default="",null=True,blank=True)
# 	cover =  models.CharField(max_length=500, verbose_name=u'封面图',default="",null=True,blank=True)
# 	content =  models.TextField( verbose_name=u'展示内容',default="",null=True,blank=True)
# 	shop_time =  models.CharField(max_length=32, verbose_name=u'营业时间',default="",null=True,blank=True)
# 	display_type =  models.IntegerField(u'展示方式',default=DISPLAY_TYPE_WX_URL,choices=DISPLAY_TYPE.items())
# 	wx_content_url =  models.CharField(max_length=500, verbose_name=u'微信展示链接',default="",null=True,blank=True)
#
# 	type =  models.IntegerField(u'类型',default=POT_TYPE_NORMAL,choices=POT_TYPE.items())
# 	latitude =  models.FloatField(max_length=100, verbose_name=u'纬度',default=0,null=True,blank=True)
# 	longitude =  models.FloatField(max_length=100, verbose_name=u'经度',default=0,null=True,blank=True)
# 	phone =  models.CharField(max_length=32, verbose_name=u'电话',default="",null=True,blank=True)
# 	address =  models.CharField(max_length=50, verbose_name=u'地址',default="",null=True,blank=True)
# 	postcode =  models.CharField(max_length=32, verbose_name=u'邮政编码',default="",null=True,blank=True)
# 	category =  models.CharField(max_length=32, verbose_name=u'目类',default="",null=True,blank=True)
# 	boundary =  models.CharField(max_length=32, verbose_name=u'范围',default="",null=True,blank=True)
# 	panoinfo =  models.CharField(max_length=100, verbose_name=u'信息',default="",null=True,blank=True)
#
# 	date =  models.CharField(max_length=100, verbose_name=u'信息',default="",null=True,blank=True)
# 	# time =  models.CharField(max_length=100, verbose_name=u'信息',default="",null=True,blank=True)
#
# 	class Meta:
# 		verbose_name_plural = verbose_name = u'店铺'
# 	def __unicode__(self):
# 		return '%s' % (self.name)
#
#
# class Trace(BaseModel):
# 	user =  models.ForeignKey( User,verbose_name=u'用户')
# 	shop =  models.ForeignKey( Shop,verbose_name=u'店铺')
#
# 	class Meta:
# 		verbose_name_plural = verbose_name = u'浏览记录'
# 	def __unicode__(self):
# 		return '%s' % (self.id)
#
#







67
