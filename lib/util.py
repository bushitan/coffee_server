#coding:utf-8
UNIT_SECOND = 86400 # 每日的秒数

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


#######积分卡模式##############
###1、积分  2、分享券  3、奖品
# 积分卡模式
SCORE_MODE_NORMAL = 1   #普通集点
SCORE_MODE_SHARE = 2    #分享集点
SCORE_MODE_PRIZE = 3    #奖品


###########店铺的图标##############
STORE_ICON_MODE_CUP = 1 #杯子图案
STORE_ICON_MODE_STAMP = 2 #印章图案
#店铺图标
STORE_ICON_MODE =  {
	STORE_ICON_MODE_CUP:u"杯子图案",
	STORE_ICON_MODE_STAMP:u"印章图案",
}
















