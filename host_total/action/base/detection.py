#coding:utf-8
from ..action_base import *
# from ..action_code import *
'''
    @class 业务权限检测
'''
class ActionDetect(ActionBase):
    def __init__(self):
        super().__init__()


    @staticmethod
    def base(func):
        def wrapper(self,request,*args, **kwargs):
            # print ("base 1234")
            return func(self,request,*args, **kwargs)
        return wrapper

    '''
        @method 检测用户
    '''
    def user_account(self,func):
        @ActionDetect.base
        def wrapper(self,request,*args, **kwargs):
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            if username == "" or password == "":
                return {
                    'code':CODE_SERVICES_LOGIN_NONE,
                }
            # 检测用户是否存在
            # if db.user.is_exists(uuid = uuid) is False:
            #     return {
            #         'message':message.user_none()
            #     }
            # 将uuid转为user_id
            # kwargs['user_id'] = db.user.get(uuid = uuid).id
            return func(self,request,*args, **kwargs)
        return wrapper

    '''
        @method 检测用户
    '''
    def user_token(self,func):
        @ActionDetect.base
        def wrapper(self,request,*args, **kwargs):
            # username = request.POST.get('username','')
            # password = request.POST.get('password','')
            # if username == "" or password == "":
            #     return {
            #         'code':CODE_SERVICES_LOGIN_NONE,
            #     }
            # 检测用户是否存在
            # if db.user.is_exists(uuid = uuid) is False:
            #     return {
            #         'message':message.user_none()
            #     }
            # 将uuid转为user_id
            # kwargs['user_id'] = db.user.get(uuid = uuid).id
            return func(self,request,*args, **kwargs)
        return wrapper
# detection = Detection()