#coding:utf-8
from lite.db.db import DB
from lite.models import *


class DBRelStoreCustomer(DB):
    def __init__(self):
        super().__init__(RelStoreCustomer)

    # 基础的查询数据
    def _pack_dict(self,object):
        print ("store:", object.store , 'customer:' ,object.customer )
        return {
            "name":object.name,
            "create_time":object.create_time.strftime("%Y-%m-%d"),

            "store_uuid":object.store.uuid,
            "title":object.store.title,
            "summary":object.store.summary,
            "description":object.store.description,
            "logo":object.store.logo,
            "icon":object.store.icon,
            "phone":object.store.phone,

            "address":object.store.address,
            "latitude":object.store.latitude,
            "longitude":object.store.longitude,

            "customer_uuid":object.customer.uuid,
            # "user_uuid":object.user.uuid,


            # "customer_uuid":object.customer.uuid,
            # "nick_name":object.nick_name,
            # "avatar_url":object.avatar_url,
            # "gender":object.gender,

            # "city":object.city,
            # "province":object.province,
            # "country":object.country,

            # "wx_openid":object.province,
            # "wx_session":object.wx_session,
            # "wx_unionid":object.wx_unionid,
        }

if __name__  == '__main__':
    import django
    django.setup()
    a= DBRelStoreCustomer()
    print ( a.filter( customer__uuid = '8e6d4c98-63d3-11e9-ad07-b83312f00bac'))
    # a.get_list(customer__uuid = '67e3f912-63d4-11e9-9b5d-b83312f00bac')
    # a.get_list(customer_id = 1)