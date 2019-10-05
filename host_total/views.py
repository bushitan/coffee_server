#coding:utf-8
from django.views.generic import ListView
from .action.action_utils import action
from  .action.action_code import *

myToken = "qwer"
'''
    @method 1 用户登录
'''
class UserLogin(ListView):
    @action.logged
    # @action.detect.user_account
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        if action.total.check_account(username,password) is False:
             return { 'code':CODE_SERVICES_LOGIN_NONE }

        user_info =  action.total.get_seller_info(username,password)
        token = user_info['wx_session']

        return {
            'data':{
                "token":token,
                "user_info":user_info,
            }
        }

'''
    @method 1.1 登陆检测
'''
class UserLoginCheck(ListView):
    @action.logged
    def post(self, request, *args, **kwargs):
        token = request.POST.get('token','')
        print (token)
        print (token == myToken)
        if action.total.check_token(token) is False:
            return { 'code':CODE_SERVICES_SESSION_NONE }
        else:
            return {}
        # return {
        #     'code':CODE_SYS_SUCCESS,
        #     'token':myToken,
        # }
        # if token == myToken:
        #     return {
        #         'code':CODE_SYS_SUCCESS,
        #         'token':myToken,
        #     }
        # else:
        #     return {
        #         'code':CODE_SERVICES_SESSION_NONE
        #     }


'''
    @method 2 综合统计数据
'''
class Total(ListView):
    @action.logged
    @action.detect.user_token
    def post(self, request, *args, **kwargs):
        store_id = request.POST.get('store_id','')
        store_info = action.total.get_store_info(store_id)
        total_dict = action.total.get_total(store_id)
        return {
            'data':{
                "store_info":store_info,
                "total_dict":total_dict,
            }
        }

        # store_info = {
        #     'longitude':108.2824409008,
        #     'latitude':22.8476540255,
        #     'name':"TJ小馆",
        # }
        # total_dict = {
        #       'day':{'score':334,'prize':23},
        #       'month':{'score':334,'prize':2233},
        #       'all':{'score':3134,'prize':223},
        # }
        # return {
        #     'data':{
        #         "store_info":store_info,
        #         "total_dict":total_dict,
        #     }
        # }

'''
    @method 3 集点地图
'''
class ScoreMap(ListView):
    @action.logged
    @action.detect.user_token
    def post(self, request, *args, **kwargs):
        store_id = request.POST.get('store_id','')
        score_list = action.total.get_map(store_id)
        return {
            'data':{
                "score_list":score_list,
            }
        }
        # score_list = [
        #     {
        #         'longitude':108.2824409008,
        #         'latitude':22.8476540255,
        #     },
        #     {
        #         'longitude':108.2824469008,
        #         'latitude':22.8476546255,
        #     },
        # ]


'''
    @method 4 销售组列表
'''
class SellerList(ListView):
    @action.logged
    @action.detect.user_token
    def post(self, request, *args, **kwargs):
        store_id = request.POST.get('store_id','')
        seller_list = action.total.get_seller_list(store_id)
        return {
            'data':{
                "seller_list":seller_list,
            }
        }

        # seller_list = [
        #     {
        #         'seller_id':1,
        #         'avartual':"qiniu.com",
        #         'name':"郭玉婷",
        #     },
        #     {
        #         'seller_id':2,
        #         'avartual':"qiniu.com",
        #         'name':"丰兄",
        #     },
        #     {
        #         'seller_id':3,
        #         'avartual':"qiniu.com",
        #         'name':"雕",
        #     },
        # ]




'''
    @method 5 销售详情
'''
class SellerDetail(ListView):
    @action.logged
    @action.detect.user_token
    def post(self, request, *args, **kwargs):
        seller_id = request.POST.get('seller_id','')
        index = request.POST.get('index','')
        range = request.POST.get('range','')
        score_list = action.total.get_score_by_seller(seller_id,index,range)
        return {
            'data':{
                "score_list":score_list,
            }
        }

        # score_list = [
        #     {
        #         'customer_id':1,
        #         'avatar_url':"https://wx.qlogo.cn/mmhead/H3fDQcWb35hvtCiaValXnC3Xs4kC7Zg8Qfa9ow0Hhm7c/132",
        #         'name':"郭玉婷",
        #         'create_time':"2019-9-15"
        #     },
        # ]