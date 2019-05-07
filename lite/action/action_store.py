#coding:utf-8
from weixin import WeixinLogin
from django.db import transaction
from lite.db.db_store import *
from lite.db.db_seller import *
from lite.db.db_customer import *
from lite.db.db_rel_store_customer import *
from lite.db.db_score import *
from lite.db.db_prize import *
from lite.db.db_share import *
from lib.util import *
# from lite.uitls.message import *

import lite.uitls.message as MSG
from lite.uitls.share_check import *
import time

class ActionStore():
    def __init__(self):
        self.db_store = DBStore()
        self.db_seller = DBSeller()
        self.db_customer = DBCustomer()
        self.db_rel_store_customer = DBRelStoreCustomer()
        self.db_score = DBScore()
        self.db_prize = DBPrize()
        self.db_share = DBShare()
    def get_info(self,store_uuid):
        return self.db_store.get_dict(uuid = store_uuid)

    def check_rel_store_customer(self,store_uuid,customer_uuid):
        if self.db_rel_store_customer.is_exists(
            store__uuid = store_uuid,
            customer__uuid = customer_uuid
        ) is False:
            store = self.db_store.get(uuid = store_uuid)
            customer = self.db_customer.get(uuid = customer_uuid)
            self.db_rel_store_customer.add(store=store,customer = customer)
        return True

    # 客户浏览店铺
    def get_store_customer_list(self,customer_uuid):
        return self.db_rel_store_customer.get_list(customer__uuid = customer_uuid)

    # 查询客户总数据
    def get_store_customer_data(self,store_uuid,customer_uuid):
        return {
            'score_num':self.db_score.count(**_rule_score(store_uuid,customer_uuid)),
            'prize_num':self.db_prize.count(**_rule_prize(store_uuid,customer_uuid)),
            'share_num':self.db_share.count(**_rule_share(store_uuid,customer_uuid)),
        }
    # 查询积分、奖品、分享券的详细数据
    def get_store_customer_score(self,store_uuid,customer_uuid):
        return self.db_score.get_list(**_rule_score(store_uuid,customer_uuid))
    def get_store_customer_prize(self,store_uuid,customer_uuid):
        return self.db_prize.get_list(**_rule_prize(store_uuid,customer_uuid))
    def get_store_customer_share(self,store_uuid,customer_uuid):
        return self.db_share.get_list(**_rule_share(store_uuid,customer_uuid))

    # def check_store_seller(self,store_uuid,seller_uuid):
    #     return self.db_seller.get_dict(uuid = seller_uuid )
        # print(self.db_seller.get_dict(uuid = seller_uuid ))
        # print(self.db_seller.get_dict(id = 1 ))
        # print(seller_uuid)
        # if self.db_seller.is_exists(uuid = seller_uuid,store__uuid = store_uuid ) is True:
        #     return {
        #         'is_seller':True,
        #         'user_info':self.db_seller.get_dict(uuid = seller_uuid,store__uuid = store_uuid )
        #     }
        # else:
        #     return  {'is_seller':False}

    def update_store(self,store_uuid,seller_uuid,*args, **kwargs):
        store = self.db_store.filter(uuid = store_uuid,)
        self.db_store.update(store,*args, **kwargs)
        return self.db_store.get_dict(uuid = store_uuid)

    # 店主增加雇员
    def add_store_employee(self,store_uuid,host_uuid,employee_uuid):
        host = self.db_seller.get(uuid = host_uuid)
        employee = self.db_seller.get(uuid = employee_uuid)
        if employee.store is None:
            self.db_seller.update( self.db_seller.filter(uuid = employee_uuid) ,store = host.store)
            return True
        else:
            print (False ,host.store_id)
            return  { "message" : u'该用户已经是店铺的销售'}

    # 店主解雇雇员
    def quit_store_employee(self,host_uuid ,employee_uuid):
         return self.db_seller.update( self.db_seller.filter(uuid = employee_uuid) ,store = None)

    # 获取seller的数据
    def get_data_seller(self,model,seller_uuid):
        # print (seller_uuid)
        seller = self.db_seller.get(uuid =seller_uuid)
        if  seller.is_host is True:
            # print (seller.store_id)
            query = { 'store': seller.store_id}  #若是店主，查看所有的数据
        else :
            query = { 'seller__uuid': seller_uuid}  # 一般员工，只能看自己的
        if model == 'score':
            return self.db_score.get_list(**query )
        if model == 'prize':
            return self.db_prize.get_list(**query )
        return self.db_share.get_list(**query )

    def get_seller_store(self,seller_uuid):
        seller = self.db_seller.get(uuid =seller_uuid)
        if seller.store is None :
            return False
        else:
            return seller.store

    def add_score(self,seller_uuid,customer_uuid):
        seller = self.db_seller.get(uuid =seller_uuid)
        customer = self.db_customer.get(uuid =customer_uuid)
        store = seller.store

        if store.mode == STORE_MODE_NORMAL:
            # 普通集点
            self.db_score.add( store = store ,seller = seller ,customer = customer )
            return True
        else :
            # 计算有效期
            share_valid_time = store.share_valid_time
            share_num = store.share_num
            now = datetime.datetime.now()
            now_stamp = time.mktime(now.timetuple())
            valid = now_stamp + share_valid_time * UNIT_SECOND
            valid_time = datetime.datetime.fromtimestamp(valid)
            # 分享集点
            self.db_share.add( store = store ,seller = seller ,customer = customer ,
                               alive = share_num,valid_time = valid_time)
            return False
        # if model == 'score':

    def add_prize(self,seller_uuid,customer_uuid):
        seller = self.db_seller.get(uuid =seller_uuid)
        customer = self.db_customer.get(uuid =customer_uuid)
        store = seller.store

        # 查询可用积分的数量
        score_count = self.db_score.count(store=store,customer=customer,is_used = False,is_delete=False)
        print ( store.exchange_value, score_count)
        if store.exchange_value <= score_count:
            with transaction.atomic():
                score_filter = self.db_score.filter(store=store,customer=customer,is_used = False,is_delete=False)
                self.db_prize.add(store = store ,seller = seller ,customer = customer) #增加奖品
                self.db_score.update(score_filter,is_used = True   )
            return True
        else:
            return False

    # 使用分享兑换积分
    def check_share_score(self,share_uuid,receive_customer_uuid):
        # alive = 0
        with transaction.atomic():
            # 基础查询信息
            share = self.db_share.get(uuid = share_uuid)
            receive_customer = self.db_customer.get(uuid =receive_customer_uuid)
            # 基础数据
            store = share.store
            seller = share.seller
            customer = share.customer
            alive = share.alive
            share_check_value = share.store.share_check_value
            share_gift_value = share.store.share_gift_value

            # 可能有点多余
            if alive <= 0:
                raise(u"已经抢完啦")

            new_alive = alive - 1

            # 获赠用户加点
            for i in range(0,share_gift_value):
                self.db_score.add( store = store ,seller = seller ,customer = receive_customer,share=share )

            # 分享拳已使用
            share_filter = self.db_share.filter(uuid = share_uuid)
            self.db_share.update(share_filter ,alive = new_alive) # 心跳减少1
            # self.db_share.update(share_filter ,receive_customer = receive_customer,)

            is_send_customer = False
            # 条件达成
            if new_alive == 0:
                # 分享用户加点
                for i in range(0,share_check_value):
                    self.db_score.add( store = store ,seller = seller ,customer = customer ,share=share )
                is_send_customer = True

            return is_send_customer,{
                "customer_score_num":share.store.share_check_value,
                "customer_uuid":share.customer.uuid,
                "receive_customer_score_num":share.store.share_gift_value,
                "receive_customer_uuid":receive_customer_uuid,
            }

# 查询积分d规则
def _rule_base(store_uuid,customer_uuid):
    return  {
        'store__uuid':store_uuid,
        'customer__uuid':customer_uuid,
    }
def _rule_score(store_uuid,customer_uuid):
    return dict(_rule_base(store_uuid,customer_uuid),**{
        'is_used':False,
    })
def _rule_prize(store_uuid,customer_uuid):
    return dict(_rule_base(store_uuid,customer_uuid),**{

    })
def _rule_share(store_uuid,customer_uuid):
    return dict(_rule_base(store_uuid,customer_uuid),**{
        # 'receive_customer':None,
        'alive__gt':0,
        'valid_time__gt':  datetime.datetime.now()
    })


if __name__  == '__main__':
    import django
    django.setup()
    a= ActionStore()
    # print (a.get_store_customer_list('8e6d4c98-63d3-11e9-ad07-b83312f00bac'))

    # r = a.check_share_score(
    #     'a2bf5542-6c0c-11e9-bd7b-b83312f00bac',
    #     '123327a6-6bf7-11e9-a5a7-b83312f00bac', # 器风了
    #     # '78ba8814-6c0b-11e9-9b35-b83312f00bac', # 未啊喂
    # )
    # print (r)

    # now = datetime.datetime.now()
    # now_stamp = time.mktime(now.timetuple())
    # valid = now_stamp + 1 * UNIT_SECOND
    # valid_time = datetime.datetime.fromtimestamp(valid)
    # print (now_stamp,valid,valid_time)
    # valid =
    # store.share_limit_time * UNIT_SECOND