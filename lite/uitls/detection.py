#coding:utf-8
import time
import lite.uitls.message as MSG
from lite.db.db_store import *
from lite.db.db_seller import *
from lite.db.db_customer import *
from lite.db.db_score import *
from lite.db.db_prize import *
from lite.db.db_share import *
db_store = DBStore()
db_seller = DBSeller()
db_customer = DBCustomer()
db_score = DBScore()
db_prize = DBPrize()
db_share = DBShare()

def base(func):
    def wrapper(self,request,*args, **kwargs):
        # uuid = request.POST.get('uuid','')
        # if uuid == '123':
        #      return MSG.view_update(), {}
        # print ("1234")
        return func(self,request,*args, **kwargs)
    return wrapper

# 用户登录检测
def user_login(func):
    @base
    def wrapper(self,request,*args, **kwargs):
        code = request.POST.get('code','')
        if code == "" or len(code) < 10: # code 防止随便输入
            return MSG.view_login_fail(), {}
        else:
            return func(self,request,*args, **kwargs)
    return wrapper

# 用户更新信息检测
def user_update(func):
    @base
    def wrapper(self,request,*args, **kwargs):
        uuid = request.POST.get('uuid','')
        is_customer = request.POST.get('is_customer','')
        if uuid == "" or is_customer == "":
            return MSG.view_update_fail(), {}
        if is_customer == 'true':
            if db_customer.is_exists(uuid = uuid) is False:
                return MSG.view_customer_none(), {}
        else:
             if db_seller.is_exists(uuid = uuid) is False:
                return MSG.view_seller_none(), {}
        return func(self,request,*args, **kwargs)
    return wrapper


# 校验店铺状态
def store_exists(func):
    @base
    def wrapper(self,request,*args, **kwargs):
        store_uuid = request.POST.get('store_uuid','')
        if db_store.is_exists(uuid = store_uuid) is False:
            return MSG.view_store_none(), {}
        if db_store.is_exists(uuid = store_uuid ,is_business=True) is False:
            return MSG.view_store_close(), {}
        return func(self,request,*args, **kwargs)
    return wrapper


# 校验顾客存在
def customer_exists(func):
    @base
    def wrapper(self,request,*args, **kwargs):
        customer_uuid = request.POST.get('customer_uuid','')
        if db_customer.is_exists(uuid = customer_uuid) is False:
            return MSG.view_customer_none(), {}
        return func(self,request,*args, **kwargs)
    return wrapper


# 校验销售存在
def seller_exists(func):
    @base
    def wrapper(self,request,*args, **kwargs):
        seller_uuid = request.POST.get('seller_uuid','')
        if db_seller.is_exists(uuid = seller_uuid) is False:
            return MSG.view_seller_none(), {}
        seller = db_seller.get(uuid = seller_uuid)
        if seller.store is None:
            return MSG.view_seller_none(), {}
        return func(self,request,*args, **kwargs)
    return wrapper

# 校验店铺和店家是否一致
def seller_host(func):
    @base
    def wrapper(self,request,*args, **kwargs):
        store_uuid = request.POST.get('store_uuid','')
        seller_uuid = request.POST.get('seller_uuid','')
        store = db_store.get(uuid = store_uuid)
        if db_seller.is_exists(uuid = seller_uuid ,store = store ,is_host = True) is False:
            return MSG.view_store_host_none(), {}
        return func(self,request,*args, **kwargs)
    return wrapper


# 校验顾客存在
def share_exists(func):
    @base
    def wrapper(self,request,*args, **kwargs):
        share_uuid = request.POST.get('share_uuid','')
        receive_customer_uuid = request.POST.get('customer_uuid',"")

        # 分享不存在
        if db_share.is_exists(uuid = share_uuid) is False:
            return MSG.share_is_none(), {}

        share = db_share.get(uuid = share_uuid)
        receive_customer = db_customer.get(uuid =receive_customer_uuid)

         # 已被领取
        if share.receive_customer is not None :
            return MSG.share_is_used() ,{}

        # 分享给自己
        if share.customer_id == receive_customer.id:
            return MSG.share_is_self() ,{}

        # 已过期
        if time.time()> time.mktime(share.valid_time.timetuple()) :
            return MSG.share_is_valid() ,{}

        # 分享的时间间隔
        last = db_share.last(receive_customer = receive_customer)
        if last is not None:
            receive_space = time.time() - time.mktime((last.receive_time.timetuple())) #接收者时间间隔
            limit_space = share.store.share_limit_time * UNIT_SECOND # 限制的时间间隔
            if receive_space < limit_space:
                return MSG.share_is_limit(limit_space - receive_space) ,{}

        return func(self,request,*args, **kwargs)
    return wrapper














