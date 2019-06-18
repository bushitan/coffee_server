#coding:utf-8

#############基础##################
UNIT_SECOND = 86400 # 每日的秒数

#图片分类
BASE_IMAGE_TYPE_COVER = 1  #封面
BASE_IMAGE_TYPE_ICON = 2	#图标
BASE_IMAGE_TYPE_QR = 3		#二维码
BASE_IMAGE_TYPE = {
	BASE_IMAGE_TYPE_COVER : 1,
	BASE_IMAGE_TYPE_ICON : 2,
	BASE_IMAGE_TYPE_QR : 3,
}

###########店铺的集点模式################
# 店铺集点模式
STORE_MODE_NORMAL = 1 #普通
STORE_MODE_SHARE = 2  #分享
STORE_MODE_ALL = 3  #普通分享并行
#店铺分享模式
STORE_MODE =  {
	STORE_MODE_NORMAL:u"普通模式",
	STORE_MODE_SHARE:u"分享模式",
    STORE_MODE_ALL:u"普通分享并行模式",
}
#自助分享全领取码有效期
STORE_AUTO_SHARE_EXPIRES = 600 #10分钟

#店铺图标
STORE_ICON_MODE_CUP = 1 #杯子图案
STORE_ICON_MODE_STAMP = 2 #印章图案
STORE_ICON_MODE =  {
	STORE_ICON_MODE_CUP:u"杯子图案",
	STORE_ICON_MODE_STAMP:u"印章图案",
}


#店铺外卖模式
STORE_WM_MODE_NORMAL = 1 #普通
STORE_WM_MODE_SHARE = 2  #分享
STORE_WM_MODE_ALL = 3  #普通分享并行
STORE_WM_MODE_CLOSE = 4  #普通分享并行
STORE_WM_MODE =  {
	STORE_WM_MODE_NORMAL:u"普通模式",
	STORE_WM_MODE_SHARE:u"分享模式",
    STORE_WM_MODE_ALL:u"普通分享并行模式",
    STORE_WM_MODE_CLOSE:u"关闭",
}

############数据模块##################
DATA_SOURCE_SCAN = 1 # 扫描来源
DATA_SOURCE_WM = 2 # 外卖来源
DATA_SOURCE =  {
	DATA_SOURCE_SCAN:u"扫描来源",
	DATA_SOURCE_WM:u"外卖来源",
}
#######积分卡模式##############
###1、积分  2、分享券  3、奖品
# 积分卡模式
SCORE_MODE_NORMAL = 1   #普通集点
SCORE_MODE_SHARE = 2    #分享集点
SCORE_MODE_PRIZE = 3    #奖品




###########地图#############
	###########Tag的服务状态#############
MAP_TAG_SERVICE_NORMAL = 1 #正常模式
MAP_TAG_SERVICE = {
	MAP_TAG_SERVICE_NORMAL:1,
}

	########文章##########
MAP_ARTICLE_TYPE_WX = 1	#微信公众号
MAP_ARTICLE_TYPE_RED = 2 #小红书
MAP_ARTICLE_TYPE_NAVIGATE = 3 #导航

MAP_ARTICLE_TYPE = {
	MAP_ARTICLE_TYPE_WX:1,
	MAP_ARTICLE_TYPE_RED:2,
	MAP_ARTICLE_TYPE_NAVIGATE:3,
}











