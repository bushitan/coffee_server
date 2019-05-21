#coding:utf-8
from lite.db.db import DBData
from lite.db.db_store import DBStore
from lite.models import *


class DBScore(DBData):
    def __init__(self):
        super().__init__(Score)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        _new = {
            "is_used":object.is_used,
            "exchange_time":object.exchange_time.strftime("%Y-%m-%d %H:%M:%S"),
            "share_id":object.share_id,
        }
        return dict(_base,**_new)

    def latest(self,customer,store):
        if self.model.objects.filter(customer = customer,store = store,)\
                .exclude(share=None).exists() is True:
            return  self.model.objects.filter(customer = customer,store = store,)\
                .exclude(share=None)[0]
        else:
            return False

    def count_valid(self,store_uuid,customer_uuid):
        db_store = DBStore()
        store = db_store.get(uuid = store_uuid)
        return self.model.objects.filter(
            store = store,
            customer__uuid = customer_uuid,
            is_used = False,
            is_delete = False,
            create_time__gt = store.start_time,
            create_time__lt = store.end_time,
        ).count()




if __name__ == '__main__':
    import django
    django.setup()
    s = DBScore()
    share = Share.objects.get(id=18)
    customer = Customer.objects.get(id=1)

    print (s.filter(seller__uuid = '6a6c8366-7606-11e9-9df9-e95aa2c51b5d'))
    # print (s.latest(customer,share.store))
    # query = { 'store_': 1}
    # l =  s.get_list(**query )
    # print (l)