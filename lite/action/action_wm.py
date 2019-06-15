#coding:utf-8

from django.db import transaction
from lite.db.db_store import *
from lite.db.db_seller import *
from lite.db.db_customer import *
from lite.db.db_rel_store_customer import *
from lite.db.db_score import *
from lite.db.db_prize import *
from lite.db.db_share import *
from lite.db.db_wm_ticket import *
from lib.util import *
import time
import datetime
import base64
import json
from lib.math_time import valid_day
class ActionWm():
    def __init__(self):
        self.db_store = DBStore()
        self.db_seller = DBSeller()
        self.db_customer = DBCustomer()
        self.db_rel_store_customer = DBRelStoreCustomer()
        self.db_score = DBScore()
        self.db_prize = DBPrize()
        self.db_share = DBShare()
        self.db_wm_ticket = DBWmTicket()

    def get_mode(self,wm_short_uuid):
        wm_ticket = self.db_wm_ticket.get(short_uuid = wm_short_uuid) #外卖漂圈
        return wm_ticket.store.wm_mode
    def get_store_uuid(self,wm_short_uuid):
        wm_ticket = self.db_wm_ticket.get(short_uuid = wm_short_uuid) #外卖漂圈
        return  {"store_uuid":wm_ticket.store.uuid}

    # 校验外卖二维码是否可以兑换领点
    def check_add_score(self,wm_short_uuid,customer_uuid):
        wm_ticket_query = self.db_wm_ticket.filter(short_uuid = wm_short_uuid) #外卖漂圈
        customer = self.db_customer.get(uuid =customer_uuid)
        wm_ticket =  wm_ticket_query[0]
        store = wm_ticket.store
        with transaction.atomic():
            # 增加集点
            for i in range(0, store.wm_check_num):
                self.db_score.add(
                    store = store ,
                    customer = customer,
                    wm_ticket = wm_ticket,
                )
            # 更新二维码使用状态
            wm_ticket_query.update(is_used = True)
        return store.wm_check_num

    # 校验外卖二维码是否可以兑换福利券
    def check_add_share(self,wm_short_uuid,customer_uuid):
        wm_ticket_query = self.db_wm_ticket.filter(short_uuid = wm_short_uuid) #外卖漂圈
        customer = self.db_customer.get(uuid =customer_uuid)
        wm_ticket =  wm_ticket_query[0]
        # 店铺信息
        store = wm_ticket.store
        with transaction.atomic():
            # 增加分享券
            self.db_share.add(
                store = store ,
                customer = customer ,
                alive = store.share_num,
                valid_time = valid_day( store.share_valid_time * UNIT_SECOND),
                wm_ticket = wm_ticket,
            )
            # 更新二维码使用状态
            wm_ticket_query.update(is_used = True)
        return store.wm_share_num

if __name__  == '__main__':
    wm = ActionWm()
       # 3smX46fZ
    # wm.check_score(
    #     wm_short_uuid='3smX46fZ',
    #     customer_uuid="1eeabca4-7156-11e9-ad02-e95aa2c51b5d"
    # )
    wm.check_share(
        wm_short_uuid='3smX46fZ',
        customer_uuid="1eeabca4-7156-11e9-ad02-e95aa2c51b5d"
    )


        # share_valid_time = store.share_valid_time
        # share_num = store.share_num
        # now = datetime.datetime.now()
        # now_stamp = time.mktime(now.timetuple())
        # valid = now_stamp + share_valid_time * UNIT_SECOND
        # valid_time = datetime.datetime.fromtimestamp(valid)














