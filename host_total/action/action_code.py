#coding:utf-8

import math
DIALOG = "1"    #提示
HIDDEN = "2"    #隐藏
HACK   = "3"      #测试

SYS = "00"    #系统
SERVICES = "01"    #系统

# 00 系统

CODE_SYS_SUCCESS = "%s%s001" %(HIDDEN,SYS)  # 正常返回，无任何提示
CODE_SYS_ERROR = "%s%s002" %(DIALOG,SYS)  #系统出错
CODE_SYS_ERROR_NETWORK = "%s%s003" %(DIALOG,SYS)  #网络错误

CODE_SERVICES_LOGIN_NONE = "%s%s001" %(DIALOG,SERVICES) # 账号密码错误
CODE_SERVICES_SESSION_NONE = "%s%s002" %(HIDDEN,SERVICES) # session没有检测到

switch = {
    CODE_SYS_SUCCESS:{'title':u"登陆成功" , 'content':u''},
    CODE_SYS_ERROR:{'title':u"系统超时" , 'content':u'请重试，如有问题请联系管理员'},
    CODE_SYS_ERROR_NETWORK:{'title':u"网络超时" , 'content':u''},
    CODE_SERVICES_LOGIN_NONE:{'title':u"信息填写不全" , 'content':u'未填写账号或密码'},
    CODE_SERVICES_SESSION_NONE:{'title':u"token已到期" , 'content':u'请重新登录'},
}

def get_code():
    return switch.keys()
def code_to_message(code,*args,**kwargs):

    if(code in switch.keys()):
        return switch[code]
    else:
        return "no message"


if __name__ == "__main__":
    print (code_to_message(CODE_SYS_SUCCESS))
    print (code_to_message(321))
    print (switch.keys())