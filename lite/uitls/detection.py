#coding:utf-8
import time
import lite.uitls.message as MSG
from lite.db.db_store import *
from lite.db.db_seller import *
from lite.db.db_customer import *
from lite.db.db_score import *
from lite.db.db_prize import *
from lite.db.db_share import *
from lite.db.db_wm_ticket import *
db_store = DBStore()
db_seller = DBSeller()
db_customer = DBCustomer()
db_score = DBScore()
db_prize = DBPrize()
db_share = DBShare()
db_wm_ticket = DBWmTicket()

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

# 店家扫描别的二维码
def scan_exists(func):
    @base
    def wrapper(self,request,*args, **kwargs):
        store_uuid = request.POST.get('store_uuid','')
        seller_uuid = request.POST.get('seller_uuid','')
        seller = db_seller.get(uuid = seller_uuid)
        if seller.store.uuid != store_uuid:
            return MSG.view_scan_none(), {}
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


# 查询分享券是否存在
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

        # 分享份数已被领取完毕
        if share.alive <= 0 :
            return MSG.share_is_used() ,{}

        # 分享给自己
        if share.customer_id == receive_customer.id:
            return MSG.share_is_self() ,{}

        # 已过期
        if time.time()> time.mktime(share.valid_time.timetuple()) :
            return MSG.share_is_valid() ,{}

        # 分享的时间间隔
        # last = db_share.last(receive_customer = receive_customer)
        # last = db_score.last(customer = receive_customer,store = share.store,share = share)
        last = db_score.latest(customer = receive_customer,store = share.store)
        if last is not False:
            receive_space = time.time() - time.mktime((last.create_time.timetuple())) #接收者时间间隔
            limit_space = share.store.share_limit_time * UNIT_SECOND # 限制的时间间隔
            if receive_space < limit_space:
                return MSG.share_is_limit(limit_space - receive_space) ,{}

        return func(self,request,*args, **kwargs)
    return wrapper

import time
# 自动分享券是否超时
def share_auto_time_out(func):
    @base
    def wrapper(self,request,*args, **kwargs):
        unix = int(request.POST.get('unix',""))
        store_id = request.POST.get('store_id',"")
        current_unix = int(time.time())
        if current_unix > unix:
             return MSG.share_is_auto_time_out(), db_store.get_dict(id = store_id)  # 返回店铺信息
        # store = db_store.get(uuid = store_uuid)
        # if db_seller.is_exists(uuid = seller_uuid ,store = store ,is_host = True) is False:
        #     return MSG.view_store_host_none(), {}
        return func(self,request,*args, **kwargs)
    return wrapper


# 校验销售是否用拥有分享券的删除权限
def seller_own_share(func):
    @base
    def wrapper(self,request,*args, **kwargs):
        share_uuid = request.POST.get('share_uuid',"")
        seller_uuid = request.POST.get('seller_uuid','')
        seller = db_seller.get(uuid = seller_uuid)
        share = db_share.get(uuid = share_uuid)
        if seller.store_id != share.store_id: # 所属店铺不一样
             return MSG.share_delete_other(), {}
        return func(self,request,*args, **kwargs)
    return wrapper

###############外卖#################
# 外卖二维码是否存在
def wm_qr_exist(func):
    @base
    def wrapper(self,request,*args, **kwargs):
        wm_short_uuid = request.POST.get('wm_short_uuid',"")
        if db_wm_ticket.is_exists(short_uuid = wm_short_uuid) is False:
            return MSG.wm_time_out(), {} # 二维码已过期
        return func(self,request,*args, **kwargs)
    return wrapper
# 外卖二维码状态校验
def wm_qr_status(func):
    @base
    def wrapper(self,request,*args, **kwargs):
        wm_short_uuid = request.POST.get('wm_short_uuid',"")

        return func(self,request,*args, **kwargs)
    return wrapper

'''
    @method 检测用户满点
    @summary 用户满点 ? 提示不能集点 : pass
'''
def wm_qr_full(func):
    @base
    def wrapper(self,request,*args, **kwargs):
        wm_short_uuid = request.POST.get('wm_short_uuid',"")
        seller_uuid = request.POST.get('seller_uuid',"")
        customer_uuid =  request.POST.get('customer_uuid',"")

        wm_ticket = db_wm_ticket.get_by_short_uuid(short_uuid = wm_short_uuid)
        kwargs['wm_ticket'] = wm_ticket
        if wm_ticket.is_used is True: #已经使用
            return MSG.wm_used(), {"store_uuid":wm_ticket.store.uuid} # 二维码已使用
        if wm_ticket.is_delete is True: #已经删除
            return MSG.wm_delete(),{"store_uuid":wm_ticket.store.uuid}# 二维码已删除

        store = {}
        if wm_short_uuid != "":
            # wm_ticket = db_wm_ticket.get_by_short_uuid(short_uuid = wm_short_uuid)
            store = wm_ticket.store
        if seller_uuid != "":
            _seller = db_seller.get(uuid = seller_uuid)
            store = _seller.store

        if store.uuid == "b29c4dee-b35e-11e9-869d-e95aa2c51b5d": # 24 strong
            if  db_score.count_valid(store.uuid,customer_uuid) >= 8:
                return MSG.wm_full(), {"store_uuid":store.uuid}
            return func(self,request,*args, **kwargs)

        if store.uuid == "a85e7854-c268-11e9-97aa-e95aa2c51b5d": # 28 seeking
            if  db_score.count_valid(store.uuid,customer_uuid) >= 6:
                return MSG.wm_full(), {"store_uuid":store.uuid}
            return func(self,request,*args, **kwargs)

        if store.uuid == "8c6e02de-3519-11ea-b35c-e95aa2c51b5d": # 58 方圆几里
            if  db_score.count_valid(store.uuid,customer_uuid) >= 16:
                return MSG.wm_full(), {"store_uuid":store.uuid}
            return func(self,request,*args, **kwargs)

        if store.uuid == "7263b5b6-0863-11ea-b6ff-e95aa2c51b5d" \
            or store.uuid == "b131ffba-b362-11e9-9abd-e95aa2c51b5d"\
            or store.uuid == "5340c542-074f-11ea-94f7-e95aa2c51b5d": # 浮梦造物\ # O.CT \ # Leisure
            if  db_score.count_valid(store.uuid,customer_uuid) >= 10:
                return MSG.wm_full(), {"store_uuid":store.uuid}
            return func(self,request,*args, **kwargs)

        if store.uuid == "3ce4a9f4-0521-11ea-b1ef-e95aa2c51b5d": # 40 CHOOSE COFFEE
            if  db_score.count_valid(store.uuid,customer_uuid) >= 12:
                return MSG.wm_full(), {"store_uuid":store.uuid}
            return func(self,request,*args, **kwargs)

        if store.uuid == "9a3e435e-62ad-11ea-95b0-e95aa2c51b5d": # 60 bai xiong coffee
            if  db_score.count_valid(store.uuid,customer_uuid) >= 15:
                return MSG.wm_full(), {"store_uuid":store.uuid}
            return func(self,request,*args, **kwargs)

        if store.uuid == "de3da45a-8a3f-11ea-89a2-e95aa2c51b5d":# 72 霸王茶姬
            if  db_score.count_valid(store.uuid,customer_uuid) >= 15:
                return MSG.wm_full(), {"store_uuid":store.uuid}
            return func(self,request,*args, **kwargs)
        score_count = db_score.count_valid(store.uuid,customer_uuid)

        print (score_count)
        if store.exchange_value <= score_count:
            return MSG.wm_full(), {"store_uuid":store.uuid}
            # return MSG.wm_full(), {"store_uuid":db_wm_ticket.get_by_short_uuid(short_uuid = wm_short_uuid).store.uuid}
        return func(self,request,*args, **kwargs)
    return wrapper

if __name__ == '__main__':
    import django
    django.setup()
    @wm_qr_full
    def test(self,re):
        pass
        # print (123)
    test(1,2)
    # print( test(1,2))



