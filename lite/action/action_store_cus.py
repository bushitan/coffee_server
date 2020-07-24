#coding:utf-8

from django.db import transaction
from lite.db.db_store import *
from lite.db.db_seller import *
from lite.db.db_customer import *
from lite.db.db_rel_store_customer import *
from lite.db.db_score import *
from lite.db.db_prize import *
from lite.db.db_share import *
from lite.db.db_ad import *
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
        self.db_ad = DBAd()

    # 检测base64
    def check_qr_base64(self,qr_base64):
        encodestr = base64.b64decode(qr_base64)
        j = json.loads( str(encodestr,'utf-8'))
        print(j['mode'])
        print(j['store_uuid'])
        print(j['seller_uuid'])
        print(j['dead_time'])
        return j

    def get_info_by_id(self,store_id ):
        return self.db_store.get_dict(id = store_id)

    # 发放福利分享券
    def get_auto_share(self,store_id,seller_id,customer_uuid):
        seller = self.db_seller.get(id =seller_id)
        customer = self.db_customer.get(uuid =customer_uuid)
        store = seller.store
        if store.id != int(store_id):
            return False

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

    '''
        @method 获取所有的挂广告
    '''
    def get_ad_list(self):
        return self.db_ad.get_show_list()

    '''
        @method 获取店铺的广告信息
    '''
    def get_current_store_ad_list(self,store_uuid):


        #  _list = self.db_ad.get_show_list()
        # if store_uuid == "54931e42-7c67-11e9-b94e-e95aa2c51b5d": # 白日梦相家
        #     _list.insert(0,{
        #         "type":AD_TYPE_IMAGE,
        #         "cover":"https://mmbiz.qpic.cn/mmbiz_jpg/49qhzgz5ydzzFxlFe6t2WicCiaXBBiarozwDt5icapj6D2q1ggCPtsrD83CpcwP2ofoW3WH76YYJKT4UMticoHdZoZw/0?wx_fmt=jpeg",
        #         "web_url":"https://mmbiz.qpic.cn/mmbiz_jpg/49qhzgz5ydzzFxlFe6t2WicCiaXBBiarozwDt5icapj6D2q1ggCPtsrD83CpcwP2ofoW3WH76YYJKT4UMticoHdZoZw/0?wx_fmt=jpeg",
        #     })
        # if store_uuid == "b29c4dee-b35e-11e9-869d-e95aa2c51b5d": # strong
        #     _list.insert(0,{
        #         "type":AD_TYPE_IMAGE,
        #         "cover":"https://mmbiz.qpic.cn/mmbiz_jpg/49qhzgz5ydzzFxlFe6t2WicCiaXBBiarozwdbjv20BTVSN2B026JgxynK8QpFrCUhiaw0u6tbTfagiaj2j65oY94QGQ/0?wx_fmt=jpeg",
        #         "web_url":"https://mmbiz.qpic.cn/mmbiz_jpg/49qhzgz5ydzzFxlFe6t2WicCiaXBBiarozwdbjv20BTVSN2B026JgxynK8QpFrCUhiaw0u6tbTfagiaj2j65oY94QGQ/0?wx_fmt=jpeg",
        #     })



        _list = self.db_ad.get_show_list()
        ad1 = {
                "type":AD_TYPE_WEB_VIEW,
                "cover":"https://mmbiz.qpic.cn/mmbiz_jpg/49qhzgz5ydzqLSa9h50XyibCENKdl5nPOdwOS99gLm89qwNkU5ZibVrFHO4hKWTpsy4QZp7c56pkCibpfTSGnibUYw/0?wx_fmt=jpeg",
                "web_url":"https://mp.weixin.qq.com/s/vUP-Oi197514DluigfRkAw",
        }
        ad2 = {
                "type":AD_TYPE_IMAGE,
                "cover":"https://mmbiz.qpic.cn/mmbiz_jpg/49qhzgz5ydzPGU3EmdXeg6yAOEZOHXGkfqMy0Jb3hks0GbOP01GKSgauENialhambiaeicFNZV0hFzBvsa2gO9b0w/0?wx_fmt=jpeg",
                "web_url":"https://mmbiz.qpic.cn/mmbiz_jpg/49qhzgz5ydzPGU3EmdXeg6yAOEZOHXGkoRyHYeG2q2NmAXdSczVxjArOJLrRBAYoSib3cJ73VZgHrqEP48VJYmA/0?wx_fmt=jpeg",
        }

        if store_uuid == "54931e42-7c67-11e9-b94e-e95aa2c51b5d": # 白日梦相家
            _list.insert(0,ad2)
            _list.insert(0,ad1)
        if store_uuid == "b29c4dee-b35e-11e9-869d-e95aa2c51b5d": # strong
            _list.insert(0,{
                "type":AD_TYPE_WEB_VIEW,
                "cover":"https://mmbiz.qpic.cn/mmbiz_jpg/49qhzgz5ydwfYkMWFDtCO0YZ3LUbZrShwJh5Wx5IWjkNBIlRHwOcgibvPA9pJPgVWbiadqd7k6mMITnx7C9UicfTQ/0?wx_fmt=jpeg",
                "web_url":"https://sj.qskjad.top/product/detail?id=bf9c8a4f-ddac-446a-9c82-885d5b664181&tjUser=7160dac4-542a-4fa7-b220-652a9358443d",
            })
            _list.insert(0,{
                "type":AD_TYPE_IMAGE,
                "cover":"https://mmbiz.qpic.cn/mmbiz_jpg/49qhzgz5ydzzFxlFe6t2WicCiaXBBiarozwdbjv20BTVSN2B026JgxynK8QpFrCUhiaw0u6tbTfagiaj2j65oY94QGQ/0?wx_fmt=jpeg",
                "web_url":"https://mmbiz.qpic.cn/mmbiz_jpg/49qhzgz5ydzzFxlFe6t2WicCiaXBBiarozwdbjv20BTVSN2B026JgxynK8QpFrCUhiaw0u6tbTfagiaj2j65oY94QGQ/0?wx_fmt=jpeg",
            })
        if store_uuid == "001fc670-f4b3-11e9-aa2b-e95aa2c51b5d": # figas
            _list.insert(0,ad2)
            _list.insert(0,ad1)
        if store_uuid == "7263b5b6-0863-11ea-b6ff-e95aa2c51b5d": # 浮梦造物
            _list.insert(0,ad2)
            _list.insert(0,ad1)
            _list.insert(0,{
                "type":AD_TYPE_WEB_VIEW,
                "cover":"https://mmbiz.qpic.cn/mmbiz_jpg/49qhzgz5ydwfYkMWFDtCO0YZ3LUbZrShIGFtbibpgic3k0DppgYQZJEcemkxR8zqvUv1GIDgSJQnKXwruZibmvrCw/0?wx_fmt=jpeg",
                "web_url":"https://mp.weixin.qq.com/s/2Oul2t7W_IFHbOveqTUwRg",
            })
        if store_uuid == "b131ffba-b362-11e9-9abd-e95aa2c51b5d": # O.CT
            _list.insert(0,ad2)
            _list.insert(0,ad1)
        if store_uuid == "5340c542-074f-11ea-94f7-e95aa2c51b5d": # Leisure
            _list.insert(0,ad2)
            _list.insert(0,ad1)
        if store_uuid == "68e54718-7156-11e9-b456-e95aa2c51b5d": # 丰丰的咖啡店
            _list.insert(0,ad2)
            _list.insert(0,ad1)

        return _list






    # 发放福利分享券（已废弃）
    # def get_auto_share11111(self,seller_uuid,customer_uuid):
    #     seller = self.db_seller.get(uuid =seller_uuid)
    #     customer = self.db_customer.get(uuid =customer_uuid)
    #     store = seller.store
    #
    #     # 计算有效期
    #     share_valid_time = store.share_valid_time
    #     share_num = store.share_num
    #     now = datetime.datetime.now()
    #     now_stamp = time.mktime(now.timetuple())
    #     valid = now_stamp + share_valid_time * UNIT_SECOND
    #     valid_time = datetime.datetime.fromtimestamp(valid)
    #     # 分享集点
    #     self.db_share.add( store = store ,seller = seller ,customer = customer ,
    #                        alive = share_num,valid_time = valid_time)
    #     return True