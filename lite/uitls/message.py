#coding:utf-8
import math
DIALOG = "1"    #提示
HIDDEN = "2"    #隐藏
HACK   = "3"      #测试

SYS = "00"    #系统
VIEW  = "01"     #公共
SCORE = "02"     #积分
PRIZE = "03"     # 礼品
SHARE = "04"    #分享
SCAN  = "05"     #扫码

# 00 系统
CODE_SYS_SUCCESS = "%s%s001" %(DIALOG,SYS)  # 正常返回，无任何提示
CODE_SYS_ERROR_NETWORK = "%s%s002" %(DIALOG,SYS)  #登陆成功
def sys_success():
    return {'code':CODE_SYS_SUCCESS,'title':u"请求成功" , 'content':u'无任何提示'}
def sys_error_network():
    return {'code':CODE_SYS_ERROR_NETWORK,'title':u"网络超时" , 'content':u''}

# 01 公共
CODE_VIEW_LOGIN = "%s%s001" %(HIDDEN,VIEW)  #登陆成功
CODE_VIEW_LOGIN_FAIL = "%s%s002" %(DIALOG,VIEW)  #登陆失败
CODE_VIEW_UPDATE = "%s%s003" %(DIALOG,VIEW)  #更新成功
CODE_VIEW_UPDATE_FAIL = "%s%s004" %(DIALOG,VIEW)  #更新成功
CODE_VIEW_CUSTOMER_NONE = "%s%s005" %(DIALOG,VIEW)  #顾客不存在
CODE_VIEW_SELLER_NONE = "%s%s006" %(DIALOG,VIEW)  #店家不存在
CODE_VIEW_STORE_NONE = "%s%s007" %(DIALOG,VIEW)  #店铺不存在
CODE_VIEW_STORE_CLOSE = "%s%s008" %(DIALOG,VIEW)  #店铺已关门
CODE_VIEW_STORE_UPDATE = "%s%s009" %(DIALOG,VIEW)  #店铺更新成功
CODE_VIEW_STORE_HOST_NONE = "%s%s010" %(DIALOG,VIEW)  #不是店铺的主人

def view_login():
    return {'code':CODE_VIEW_LOGIN,'title':u"登陆成功" , 'content':u''}
def view_login_fail():
    return {'code':CODE_VIEW_LOGIN_FAIL,'title':u"登陆失败" , 'content':u'请传入完整参数'}
def view_update():
    return {'code':CODE_VIEW_UPDATE,'title':u"更新信息成功" , 'content':u''}
def view_update_fail():
    return {'code':CODE_VIEW_UPDATE,'title':u"更新信息失败" , 'content':u'请传入完整参数'}

def view_customer_none():
    return {'code':CODE_VIEW_CUSTOMER_NONE,'title':u"顾客不存在" , 'content':u'请从小程序登陆'}
def view_seller_none():
    return {'code':CODE_VIEW_SELLER_NONE,'title':u"店家不存在" , 'content':u'请从商户端小程序登陆'}
def view_store_none():
    return {'code':CODE_VIEW_STORE_NONE,'title':u"店铺不存在" , 'content':u'请从小程序登陆'}
def view_store_close():
    return {'code':CODE_VIEW_STORE_CLOSE,'title':u"店铺已关门" , 'content':u'请从小程序登陆'}
def view_store_update():
    return {'code':CODE_VIEW_STORE_UPDATE,'title':u"更新成功" , 'content':u'店铺数据已更新'}
def view_store_host_none():
    return {'code':CODE_VIEW_STORE_HOST_NONE,'title':u"您不是该店铺的主人" , 'content':u''}

# 02 积分
CODE_SCORE_SUCCESS = "%s%s001" %(DIALOG,SCORE)  #积分成功
def score_success():
    return {'code':CODE_SCORE_SUCCESS,'title':u"集点成功" , 'content':u''}

# 03 礼品
CODE_PRIZE_SUCCESS = "%s%s001" %(DIALOG,PRIZE)  #积分成功
def prize_success():
    return {'code':CODE_PRIZE_SUCCESS,'title':u"兑换礼物成功" , 'content':u'请跟店家领取礼物哦'}

# 04 分享券
CODE_SHARE_SEND      = "%s%s001" %(DIALOG,SHARE)  #赠送成功
CODE_SHARE_RECEIVE   = "%s%s002" %(DIALOG,SHARE)  #获得成功
CODE_SHARE_NONE      = "%s%s003" %(DIALOG,SHARE)  #不存在
CODE_SHARE_USED      = "%s%s004" %(DIALOG,SHARE)  #已领取
CODE_SHARE_SELF      = "%s%s005" %(DIALOG,SHARE)  #不能领取自己的券
CODE_SHARE_LIMIT     = "%s%s006" %(DIALOG,SHARE)  #限制期间，重复领取
CODE_SHARE_VALID     = "%s%s007" %(DIALOG,SHARE)  #券已过期

SHARE_FAIL = u'领取失败'
def share_send(score):
    return {'code':CODE_SHARE_SEND,'title':u"分享好友成功" , 'content':u'获得了%s点' %(score)}
def share_receive():
    return {'code':CODE_SHARE_SEND,'title':u"领取分享成功" , 'content':u''}
def share_is_none():
    return {'code':CODE_SHARE_NONE,'title':SHARE_FAIL , 'content':u'分享券不存在'}
def share_is_used():
    return {'code':CODE_SHARE_USED,'title':SHARE_FAIL , 'content':u'分享券已经被领取'}
def share_is_self():
    return {'code':CODE_SHARE_SELF,'title':SHARE_FAIL , 'content':u'这是您自己的分享券，邀请好友同分享'}
def share_is_limit(date):
    hour = (date/3600)
    if hour < 24:
        d = "%s小时" %( math.ceil(hour))
    else:
        day = hour / 24
        d = "%s天" %( math.ceil(day))
    return {'code':CODE_SHARE_LIMIT,'title':SHARE_FAIL , 'content':u'请在%s之后继续领取'%(d) }
def share_is_valid():
    return {'code':CODE_SHARE_VALID,'title':SHARE_FAIL , 'content':u'分享券已过期'}

# 05 扫码
CODE_SCAN_SCORE      = "%s%s001" %(DIALOG,SCAN)  #发放集点
CODE_SCAN_PRIZE      = "%s%s002" %(DIALOG,SCAN)  #兑换礼物
CODE_SCAN_SHARE      = "%s%s003" %(DIALOG,SCAN)  #发放分享券
CODE_SCAN_PRIZE_USED      = "%s%s004" %(DIALOG,SCAN)  #礼品已经发放
def scan_score():
    return {'code':CODE_SCAN_SCORE,'title':u"发放集点成功" , 'content':u''}
def scan_prize():
    return {'code':CODE_SCAN_PRIZE,'title':u"发放礼物成功" , 'content':u''}
def scan_share():
    return {'code':CODE_SCAN_SHARE,'title':u"发放分享券成功" , 'content':u''}
def scan_prize_none():
    return {'code':CODE_SCAN_PRIZE_USED,'title':u"兑换失败" , 'content':u'兑换奖品所需点数不够'}

