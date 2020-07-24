#coding:utf-8
from django.views.generic import ListView
from lib.logged import logged
import lite.uitls.message as MSG
import lite.uitls.detection as det

from lite.action.action_user import *
action_seller = ActionSeller()
action_customer = ActionCustomer()
from lite.action.action_store import *
action_store = ActionStore()
from lite.action.action_store_cus import *
action_store_cus = ActionStoreCus()
from lite.action.action_wm import *
action_wm = ActionWm()

from lib.info_map import *
info_map = InfoMap()
from lib.util import *




from lite.action.action_test import *
action_test = ActionTest()
import base64
# @test
class ErrorTest(ListView):
    @logged
    def post(self, request, *args, **kwargs):

        nick_name = request.POST.get('nickName','')
        nick_name = base64.b64encode(nick_name.encode('utf-8'))
        print (nick_name)

        decode =  base64.b64decode(nick_name)
        print (decode)


        action_test.t1()
        return MSG.sys_success(),{}
        # raise (u"shaidhsa 粗哦无敌")


# @log
class UserLogin(ListView):
    @logged
    @det.user_login
    def post(self, request, *args, **kwargs):
        code = request.POST.get('code','')
        uuid = request.POST.get('uuid','')
        is_customer = request.POST.get('is_customer','')
        if is_customer == 'true':
            action_user = action_customer
        else:
            action_user =  action_seller
        user_info = action_user.checkSession(code,uuid)
        return MSG.view_login(), user_info

# 更新用户信息
class UserUpdate(ListView):
    @logged
    @det.user_update
    def post(self, request, *args, **kwargs):
        uuid = request.POST.get('uuid','')
        is_customer = request.POST.get('is_customer','')
        if is_customer == 'true':
            action_user = action_customer
        else:
            action_user =  action_seller
        user_info = action_user.update_user_info(
            uuid,
            # nick_name = request.POST.get('nickName',''), # 不再用nick_name 做存储
            nick_name = request.POST.get('nickName',''),
            avatar_url = request.POST.get('avatarUrl',''),
            gender =request.POST.get('gender',''),
            city =request.POST.get('city',''),
            province = request.POST.get('province',''),
            country = request.POST.get('country','')
        )
        return  MSG.view_update(),user_info

# 获取店铺信息
class StoreInfo(ListView):
    @logged
    @det.store_exists
    def post(self, request, *args, **kwargs):
        store_uuid = request.POST.get('store_uuid',"")
        seller_uuid = request.POST.get('seller_uuid',"")
        customer_uuid = request.POST.get('customer_uuid',"")
        if customer_uuid != "":
            action_store.check_rel_store_customer(store_uuid,customer_uuid)
        return MSG.sys_success(), action_store.get_info(store_uuid)

# 客户获取已经浏览的列表
class CustomerStore(ListView):
    @logged
    @det.customer_exists
    def post(self, request, *args, **kwargs):
        customer_uuid = request.POST.get('customer_uuid',"")
        return  MSG.sys_success(),action_store.get_store_customer_list(customer_uuid)

# 客户在该店铺下的积分数据
class CustomerData(ListView):
    @logged
    @det.store_exists
    @det.customer_exists
    def post(self, request, *args, **kwargs):
        store_uuid = request.POST.get('store_uuid',"")
        customer_uuid = request.POST.get('customer_uuid',"")
        return  MSG.sys_success(),action_store.get_store_customer_data(store_uuid,customer_uuid)

# 客户在该店铺下的详细数据
class CustomerDetail(ListView):
    @logged
    @det.store_exists
    @det.customer_exists
    def post(self, request, *args, **kwargs):
        model = request.POST.get('model',"score") # 默认查询积分
        store_uuid = request.POST.get('store_uuid',"")
        customer_uuid = request.POST.get('customer_uuid',"")
        if model == 'score':
            return MSG.sys_success(),action_store.get_store_customer_score(store_uuid,customer_uuid)
        if model == 'prize':
            return MSG.sys_success(),action_store.get_store_customer_prize(store_uuid,customer_uuid)
        return MSG.sys_success(),action_store.get_store_customer_share(store_uuid,customer_uuid)


# 领取好友分享券
class CustomerShare(ListView):
    @logged
    @det.customer_exists
    @det.share_exists
    def post(self, request, *args, **kwargs):
        share_uuid = request.POST.get('share_uuid',"")
        receive_customer_uuid = request.POST.get('customer_uuid',"")
        is_send_customer , message = action_store.check_share_score(share_uuid,receive_customer_uuid)
        # 是否通知分享人
        if is_send_customer is True:
            info_map.add( message['customer_uuid'],MSG.share_send(message['customer_score_num']))
        return MSG.share_receive(message['receive_customer_score_num']),{}

# 客户在定时刷新自己的信息
class CustomerRefresh(ListView):
    @logged
    @det.customer_exists
    def post(self, request, *args, **kwargs):
        customer_uuid = request.POST.get('customer_uuid',"")
        return MSG.sys_success(), {
            'info_list':info_map.pop(customer_uuid)
        }


# 客户自助扫二维码领券
class CustomerScanAutoShare(ListView):
    @logged
    @det.customer_exists
    @det.share_auto_time_out
    def post(self, request, *args, **kwargs):
        # TODO store_id
        store_id = request.POST.get('store_id',"")
        seller_id =  request.POST.get('seller_id',"")
        # unix =  request.POST.get('unix',"")
        customer_uuid = request.POST.get('customer_uuid',"")
        r = action_store_cus.get_auto_share(store_id,seller_id,customer_uuid)
        if r is True :
            return MSG.share_success(), action_store_cus.get_info_by_id(store_id)
        else:
            return MSG.share_is_auto_error() ,{}


# 外卖模式--客户自助扫领取
class CustomerScanWm(ListView):
    @logged
    @det.customer_exists
    @det.wm_qr_exist
    # @det.wm_qr_status
    @det.wm_qr_full
    def post(self, request, *args, **kwargs):
        wm_short_uuid = request.POST.get('wm_short_uuid',"")
        customer_uuid =  request.POST.get('customer_uuid',"")


        # mode = action_wm.get_store_mode(wm_short_uuid)
        # call_back_data =  action_wm.get_store_uuid(wm_short_uuid)

        wm_ticket = kwargs['wm_ticket']

        mode = wm_ticket.store.wm_mode
        call_back_data = {"store_uuid":wm_ticket.store.uuid}

        # 仅仅剩积分模式
        score_num = action_wm.check_add_score(wm_ticket,customer_uuid)
        return MSG.wm_score(score_num) ,call_back_data

        # # 店铺模式
        # if mode == STORE_WM_MODE_NORMAL : #积分模式
        #     score_num = action_wm.check_add_score(wm_ticket,customer_uuid)
        #     return MSG.wm_score(score_num) ,call_back_data
        # elif mode == STORE_WM_MODE_SHARE: #分享模式
        #     share_num = action_wm.check_add_share(wm_short_uuid,customer_uuid)
        #     return MSG.wm_share(share_num) ,call_back_data
        # elif mode == STORE_WM_MODE_ALL: #并行模式
        #     score_num = action_wm.check_add_score(wm_ticket,customer_uuid)
        #     share_num = action_wm.check_add_share(wm_short_uuid,customer_uuid)
        #     return MSG.wm_all(score_num,share_num) ,call_back_data
        # elif mode == STORE_WM_MODE_SELF: #根据门票type
        #
        #     # 门票自身模式
        #     ticket_type = action_wm.get_type(wm_short_uuid)
        #     if ticket_type == TICKET_TYPE_SCORE:
        #         score_num = action_wm.check_add_score(wm_ticket,customer_uuid)
        #         return MSG.wm_score(score_num) ,call_back_data
        #     elif ticket_type == TICKET_TYPE_SHARE:
        #         share_num = action_wm.check_add_share(wm_short_uuid,customer_uuid)
        #         return MSG.wm_share(share_num) ,call_back_data
        #     elif ticket_type == TICKET_TYPE_DOUBLE:
        #         score_num = action_wm.check_add_score(wm_ticket,customer_uuid)
        #         share_num = action_wm.check_add_share(wm_short_uuid,customer_uuid)
        #         return MSG.wm_all(score_num,share_num) ,call_back_data
        #     else : #门票自身卖已关闭
        #         return MSG.wm_close() ,{}
        #外卖已关闭
        # else :
        #     return MSG.wm_close() ,{}

# 检测信息
class CustomerScanWmCheck(ListView):
    @logged
    @det.wm_qr_exist
    def post(self, request, *args, **kwargs):
        wm_short_uuid = request.POST.get('wm_short_uuid',"")
        return MSG.sys_success() ,action_wm.get_ticket_info(wm_short_uuid)


# # 客户端获取广告
# class CustomerGetAd(ListView):
#     @logged
#     def post(self, request, *args, **kwargs):
#         return MSG.sys_success() ,action_store_cus.get_ad_list()

# 客户端获取广告
class CustomerGetAdByStore(ListView):
    @logged
    def post(self, request, *args, **kwargs):
        store_uuid = request.POST.get('store_uuid',"")
        # return MSG.sys_success() ,{'ad':action_store_cus.get_current_store_ad_list(store_uuid)}
        return MSG.sys_success() ,action_store_cus.get_current_store_ad_list(store_uuid)


# 客户自助扫二维码领券(已废弃）
# class CustomerScanAutoShare111111(ListView):
#     @logged
#     @det.customer_exists
#     def post(self, request, *args, **kwargs):
#         # 二维码分享--废弃
#         customer_uuid = request.POST.get('customer_uuid',"")
#         qr_base64 = request.POST.get('qr_base64',"")
#         qr_json = action_store_cus.check_qr_base64(qr_base64)
#         seller_uuid = qr_json['seller_uuid']
#         action_store_cus.get_auto_share(seller_uuid,customer_uuid)
#         return MSG.share_success(), {}


        # print (customer_uuid,qr_base64)
        # return MSG.sys_success(), {}



# # 判断商户身份
# class SellerCheck(ListView):
#     @logged
#     def post(self, request, *args, **kwargs):
#         store_uuid = request.POST.get('store_uuid','')
#         seller_uuid = request.POST.get('seller_uuid','')
#         return action_store.check_store_seller(store_uuid, seller_uuid)


# 客户在更新店铺下的详细数据
class SellerUpdate(ListView):
    @logged
    @det.store_exists
    @det.seller_host
    def post(self, request, *args, **kwargs):
        store_uuid = request.POST.get('store_uuid','')
        seller_uuid = request.POST.get('seller_uuid','')
        print(store_uuid)
        print(seller_uuid)
        key_list = ['title','summary','description','logo','icon','phone','address','latitude','longitude',
                    'mode','exchange_value','check_value',
                    'share_check_value','share_gift_value','share_num','share_limit_time','share_valid_time',]
        key_dict = {}
        for key in key_list:
            value = request.POST.get(key,"")
            if value != "":
                key_dict[key] = value
        return  MSG.view_store_update(), action_store.update_store(store_uuid, seller_uuid, **key_dict)

# 查积分
class SellerData(ListView):
    @logged
    @det.seller_exists
    def post(self, request, *args, **kwargs):
        model = request.POST.get('model','score')
        seller_uuid = request.POST.get('seller_uuid','')
        page_num = int( request.POST.get('page_num',0))
        range = int(request.POST.get('range',10))
        print (page_num,range)
        return MSG.sys_success(),action_store.get_data_seller(model,seller_uuid,page_num,range)

# 查店主总数
class SellerHostData(ListView):
    @logged
    @det.seller_exists
    @det.seller_host
    def post(self, request, *args, **kwargs):
        store_uuid = request.POST.get('store_uuid','')
        # seller_uuid = request.POST.get('seller_uuid','')
        return MSG.sys_success(),action_store.get_host_data(store_uuid)

# 获取自助分享模式二维码
class SellerAutoShareQR(ListView):
    @logged
    @det.seller_exists
    def post(self, request, *args, **kwargs):
        # store_uuid = request.POST.get('store_uuid','')
        seller_uuid = request.POST.get('seller_uuid','')
        # print(seller_uuid)
        qr_data = action_store.get_auto_share_qr_data(seller_uuid)
        # 生成自助二维码
        access_token = action_customer.get_access_token()
        qr = action_customer.get_un_limit_qr( access_token ,qr_data )
        return MSG.sys_success(),{'token': action_customer.get_access_token(),"qr":qr}
        # seller_uuid = request.POST.get('seller_uuid','')
        # data = {
        #     "scene":"sdfghjkl",
        #     "page":"pages/route/route",
        # }

    # 获取自助分享模式二维码
class SellerShareDelete(ListView):
    @logged
    @det.seller_exists
    @det.seller_own_share
    def post(self, request, *args, **kwargs):
        share_uuid = request.POST.get('share_uuid',"")
        seller_uuid = request.POST.get('seller_uuid','')
        action_store.delete_share(share_uuid)
        return MSG.share_delete(),{}


# 扫码
class SellerScan(ListView):
    @logged
    @det.seller_exists
    @det.customer_exists
    @det.scan_exists
    def post(self, request, *args, **kwargs):
        model = request.POST.get('model','score')
        store_uuid = request.POST.get('store_uuid','')
        seller_uuid = request.POST.get('seller_uuid','')
        customer_uuid = request.POST.get('customer_uuid','')
        if model == 'score': # 发放积分 or 分享券
            is_score = action_store.add_score(seller_uuid,customer_uuid)
            if is_score:
                info_map.add( customer_uuid,MSG.score_success())
                return MSG.scan_score(),{}
            else :
                info_map.add( customer_uuid,MSG.share_success())
                return MSG.scan_share(),{}
        else:# 兑换奖品
        # if model == 'prize':
            is_success = action_store.add_prize(seller_uuid,customer_uuid)
            if is_success:
                info_map.add( customer_uuid,MSG.prize_success())
                return MSG.scan_prize(),{}
            else:
                return MSG.scan_prize_none(),{}


# 扫码集点
class SellerScanScore(ListView):
    @logged
    @det.seller_exists
    @det.customer_exists
    @det.scan_exists
    @det.wm_qr_full
    def post(self, request, *args, **kwargs):
        seller_uuid = request.POST.get('seller_uuid','')
        customer_uuid = request.POST.get('customer_uuid','')
        action_store.add_score(seller_uuid,customer_uuid)
        info_map.add( customer_uuid,MSG.score_success())
        return MSG.scan_score(),{}

# 发放分享券
class SellerScanShare(ListView):
    @logged
    @det.seller_exists
    @det.customer_exists
    @det.scan_exists
    def post(self, request, *args, **kwargs):
        seller_uuid = request.POST.get('seller_uuid','')
        customer_uuid = request.POST.get('customer_uuid','')
        action_store.add_share(seller_uuid,customer_uuid)
        info_map.add( customer_uuid,MSG.share_success())
        return MSG.scan_share(),{}

# 兑换福利
class SellerScanPrize(ListView):
    @logged
    @det.seller_exists
    @det.customer_exists
    @det.scan_exists
    def post(self, request, *args, **kwargs):
        seller_uuid = request.POST.get('seller_uuid','')
        customer_uuid = request.POST.get('customer_uuid','')
        is_success = action_store.add_prize(seller_uuid,customer_uuid)
        if is_success:
            info_map.add( customer_uuid,MSG.prize_success())
            return MSG.scan_prize(),{}
        else:
            return MSG.scan_prize_none(),{}




# 检测信息
class PrintGetWMList(ListView):
    @logged
    # @det.wm_qr_exist
    def post(self, request, *args, **kwargs):
        token = request.POST.get('token',"")
        start = request.POST.get('start',"")
        end = request.POST.get('end',"")

        # 强制token
        if token != "bushitan":
            return MSG.scan_prize_none(),{}
        wm_list = action_wm.get_ticket_start_end(start,end)
        return MSG.sys_success() ,{
            "wm_list":wm_list
        }











        # if model == 'score': # 发放积分 or 分享券
        #     is_score = action_store.add_score(seller_uuid,customer_uuid)
        #     if is_score:
        #         info_map.add( customer_uuid,MSG.score_success())
        #         return MSG.scan_score(),{}
        #     else :
        #         info_map.add( customer_uuid,MSG.share_success())
        #         return MSG.scan_share(),{}
        # else:# 兑换奖品
        # # if model == 'prize':
        #     is_success = action_store.add_prize(seller_uuid,customer_uuid)
        #     if is_success:
        #         info_map.add( customer_uuid,MSG.prize_success())
        #         return MSG.scan_prize(),{}
        #     else:
        #         return MSG.scan_prize_none(),{}

        # # 核查销售权限
        # store = action_store.get_seller_store(seller_uuid)
        # if store is False:
        #     return { 'message': u'您没有核销权限'}

        # 根据uuid
        # store_uuid = store.id



        # if model == 'prize':
        #     return self.db_prize.get_list(**query )
        # if model == 'share':
        #     return self.db_share.get_list(**query )
        # return action_store.scan(model,seller_uuid,customer_uuid)











# 商家邀请雇员
class SellerInvite(ListView):
    @logged
    def post(self, request, *args, **kwargs):
        store_uuid = request.POST.get('store_uuid','')
        host_uuid = request.POST.get('host_uuid','')
        employee_uuid = request.POST.get('employee_uuid','')
        return action_store.add_store_employee(store_uuid, host_uuid, employee_uuid)


# 雇员解散店铺
class SellerQuit(ListView):
    @logged
    def post(self, request, *args, **kwargs):
        host_uuid = request.POST.get('host_uuid','')
        employee_uuid = request.POST.get('employee_uuid','')
        return action_store.quit_store_employee( host_uuid ,employee_uuid)















# @log
class Index55(ListView):
    @logged
    def post(self, request, *args, **kwargs):
        code = request.POST.get('code',"")
        uuid = request.POST.get('uuid',"")
        user_info = action_customer.checkSession(code,uuid)
        return user_info






        # print( self.__class__.__name__)

# def log(func):
#     @functools.wraps(func)
#     def wrapper1(*args, **kwargs):
#         try:
#             # print( 1,self)
#             print( 1,*args, **kwargs)
#             print( kwargs.get('a',None))
#             print( 'call %s():' % func.__class__.__name__)
#             _dict = func(*args, **kwargs)
#             # return _dict
#             return HttpResponse( json.dumps( _dict ),content_type="application/json" )
#         except BaseException as e:
#             _dict = {
#                 "error":str(e)
#             }
#             print (_dict)
#             # return _dict
#             return HttpResponse( json.dumps( _dict ),content_type="application/json" )
#     return wrapper1

#
# class Decorator(object):
#     def __init__(self, f):
#         self.f = f
#     def __call__(self,*args, **kwargs):
#         print("decorator start")
#         print ('2 call1 %s():' % self.__class__.__name__)
#         self.f(*args, **kwargs)
#         print("decorator end")
#         def aa(*args, **kwargs):
#             return 123
#         return aa

        # print (2,_dict)
        # return _dict
        # return HttpResponse( json.dumps( _dict ),content_type="application/json" )








        # raise (123)
        # return HttpResponse( json.dumps( _dict ),content_type="application/json" )
            # try:
            #     _str_hash = request.POST['hash']
            #     _dict = {
            #         'MSG':u'登录初始化成狗',
            #     }
            #     return MESSAGE_RESPONSE_SUCCESS(_dict)
            # except Exception,e :
            #     return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

    # def get_context_data(self, **kwargs):
    #     return super(Index, self).get_context_data(**kwargs)
    # def get_queryset(self):
    #     pass