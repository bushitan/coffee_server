#coding:utf-8

from lite.db.db_wm_ticket import *
from lite.action.action_user import *
action_customer = ActionCustomer()
from lite.action.action_wm import *
action_wm = ActionWm()

class WmCreate:
    def __init__(self):
        pass

    # 根据店铺，创造二维码
    def get_qr(self,store_uuid):

        #DOTO
        qr_data = action_wm.get_ticket_qr(store_uuid)
        access_token = action_customer.get_access_token()
        qr = action_customer.get_wm_qr( access_token ,qr_data )
        return qr
        # return access_token
        # return MSG.sys_success(),{'token': action_customer.get_access_token(),"qr":qr}

if __name__  == '__main__':
    wc = WmCreate()
    for i in range(0,50):
        t = wc.get_qr(store_uuid="68e54718-7156-11e9-b456-e95aa2c51b5d")
        print (t)