#coding:utf-8

from django.db import transaction
from lite.db.db_store import *
from lite.db.db_seller import *
from lite.db.db_customer import *
from lite.db.db_rel_store_customer import *
from lite.db.db_score import *
from lite.db.db_prize import *
from lite.db.db_share import *
from lib.util import *
import time
import datetime
import base64
import json

class ActionStoreCus():
    def __init__(self):
        self.db_store = DBStore()
        self.db_seller = DBSeller()
        self.db_customer = DBCustomer()
        self.db_rel_store_customer = DBRelStoreCustomer()
        self.db_score = DBScore()
        self.db_prize = DBPrize()
        self.db_share = DBShare()

    # 检测base64
    def check_qr_base64(self,qr_base64):
        encodestr = base64.b64decode(qr_base64)
        j = json.loads( str(encodestr,'utf-8'))
        print(j['mode'])
        print(j['store_uuid'])
        print(j['seller_uuid'])
        print(j['dead_time'])
        return j


    # 发放福利分享券
    def get_auto_share(self,seller_uuid,customer_uuid):
        seller = self.db_seller.get(uuid =seller_uuid)
        customer = self.db_customer.get(uuid =customer_uuid)
        store = seller.store

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
        return True