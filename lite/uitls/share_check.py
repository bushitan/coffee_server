#coding:utf-8
# from lite.uitls.message import  *
import lite.uitls.message as MSG
import datetime
import time

class ShareCheck():
    title = "领取成功"
    content = "您"
    def __init__(self,share,receive_customer):
        self.share = share
        self.receive_customer = receive_customer


    def result(self):
        # 已被领取
        if self.share.receive_customer is not None :
            return False,MSG.share_is_used()
        # 分享给自己
        if self.share.customer_id == self.receive_customer.id:
            return False,MSG.share_is_self()
        # 已过期
        if time.time()> time.mktime(self.share.valid_time.timetuple()) :
            return False,MSG.share_is_valid()

        return True ,"" # 默认为true

    # def result(self):
    #     return self._process()