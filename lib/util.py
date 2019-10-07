#coding:utf-8

#############基础##################
UNIT_SECOND = 86400 # 每日的秒数

#图片分类
BASE_IMAGE_TYPE_COVER = 1  #封面
BASE_IMAGE_TYPE_ICON = 2	#图标
BASE_IMAGE_TYPE_QR = 3		#二维码
BASE_IMAGE_TYPE_AD_CONTENT = 4		#广告内容
BASE_IMAGE_TYPE = {
	BASE_IMAGE_TYPE_COVER : u'封面',
	BASE_IMAGE_TYPE_ICON : u'图标',
	BASE_IMAGE_TYPE_QR : u'二维码',
	BASE_IMAGE_TYPE_AD_CONTENT : u'广告内容',
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
STORE_ICON_MODE_LADDER = 3 #印章图案
STORE_ICON_MODE =  {
	STORE_ICON_MODE_CUP:u"杯子图案",
	STORE_ICON_MODE_STAMP:u"印章图案",
	STORE_ICON_MODE_LADDER:u"天梯图案",
}


#店铺外卖模式
STORE_WM_MODE_NORMAL = 1 #普通
STORE_WM_MODE_SHARE = 2  #分享
STORE_WM_MODE_ALL = 3  #普通分享并行
STORE_WM_MODE_CLOSE = 4  #普通分享并行
STORE_WM_MODE_SELF = 5  #根据门票的信息自定义
STORE_WM_MODE =  {
	STORE_WM_MODE_NORMAL:u"普通模式",
	STORE_WM_MODE_SHARE:u"分享模式",
    STORE_WM_MODE_ALL:u"普通分享并行模式",
    STORE_WM_MODE_SELF:u"据门票的类别自定义",
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


'''
	WmTicket门票的类型
'''
TICKET_TYPE_SCORE = 1  #积分
TICKET_TYPE_SHARE = 2	#分享
TICKET_TYPE_DOUBLE = 3	#并行
TICKET_TYPE_CLOSE = 4  #关闭
TICKET_TYPE = {
	TICKET_TYPE_SCORE : u'积分码',
	TICKET_TYPE_SHARE : u'分享码',
	TICKET_TYPE_DOUBLE : u'积分与分享共码',
    TICKET_TYPE_CLOSE:u"关闭",
}

'''
	WmTicket门票的来源
'''
TICKET_SOURCE_SCAN = 1 # 扫描来源
TICKET_SOURCE_MAP = 2 # 地图来源
TICKET_SOURCE =  {
	TICKET_SOURCE_SCAN:u"扫描来源",
	TICKET_SOURCE_MAP: u"地图来源",
}



###########地图#############
	###########Tag的服务状态#############
MAP_TAG_SERVICE_NORMAL = 1 #正常模式
MAP_TAG_SERVICE = {
	MAP_TAG_SERVICE_NORMAL:u"正常模式",
}

	#文章
MAP_ARTICLE_TYPE_WX = 1	#微信公众号
MAP_ARTICLE_TYPE_RED = 2 #小红书
MAP_ARTICLE_TYPE_NAVIGATE = 3 #导航

MAP_ARTICLE_TYPE = {
	MAP_ARTICLE_TYPE_WX:u'微信公众号',
	MAP_ARTICLE_TYPE_RED:u'小红书',
	MAP_ARTICLE_TYPE_NAVIGATE:u'实景导航',
}

###########地图#############
MAP_VISITOR_TYPE_AUTHOR = 1
MAP_VISITOR_TYPE_NORMAL = 2
MAP_VISITOR_TYPE = {
	MAP_VISITOR_TYPE_AUTHOR:u'博主',
	MAP_VISITOR_TYPE_NORMAL:u'路人',
}



#############广告 统计################
AD_TYPE_IMAGE = 1
AD_TYPE_WEB_VIEW = 2
AD_TYPE_LITE = 3
AD_TYPE = {
	AD_TYPE_IMAGE:u'图片',
	AD_TYPE_WEB_VIEW:u'浏览网页',
	AD_TYPE_LITE:u'打开小程序',
}



COLLECT_TYPE_BASE = 1
COLLECT_TYPE_AD = 2
COLLECT_TYPE_WM = 3
COLLECT_TYPE_SCAN_STORE = 4
# 收集数据的模式
COLLECT_TYPE = {
	COLLECT_TYPE_BASE:u"基础统计，无类别",
	COLLECT_TYPE_AD:u"广告点击",
	COLLECT_TYPE_WM:u"外卖扫码",
	COLLECT_TYPE_SCAN_STORE:u"台卡扫码",
}




