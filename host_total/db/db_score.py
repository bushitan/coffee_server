#coding:utf-8
from lite.db.db import DBData
from lite.db.db_store import DBStore
from lite.models import *
import datetime

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

    '''
        @method 用户可用点数
        @summary 查询店铺有效期内的点数，有效期范围外的不计入
        @param
            store_uuid    店铺uuid
            customer_uuid 顾客uuid
        @return 有效总数
    '''
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


    def get_statistic(self,store_uuid):
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        month_start = today.strftime('%Y-%m') + "-01"
        return {
            'day': self.model.objects.filter(store__uuid=store_uuid,create_time__range=[today, tomorrow]).count(),
            'month':self.model.objects.filter(store__uuid=store_uuid,create_time__range=[month_start, tomorrow]).count(),
            'all':self.model.objects.filter(store__uuid=store_uuid).count(),
        }

    # 获取当天的积分情况
    def get_today(self,store_uuid):
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        score_filter = self.model.objects.filter(store__uuid=store_uuid,create_time__range=[today, tomorrow])
        return self._pack_list( self._pack_dict,score_filter)


if __name__ == '__main__':
    import django
    django.setup()
    s = DBScore()
    share = Share.objects.get(id=18)
    customer = Customer.objects.get(id=1)
    score = Score.objects.filter(seller__uuid = '6a6c8366-7606-11e9-9df9-e95aa2c51b5d')[0:10]
    print( score)
    # print (s.filter(seller__uuid = '6a6c8366-7606-11e9-9df9-e95aa2c51b5d'))
    # print (s.latest(customer,share.store))
    # query = { 'store_': 1}
    # l =  s.get_list(**query )
    # print (l)