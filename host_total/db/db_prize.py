#coding:utf-8
from lite.db.db import DBData
from lite.models import *

import datetime

class DBPrize(DBData):
    def __init__(self):
        super().__init__(Prize)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        _new = {
        }
        return dict(_base,**_new)


    def get_statistic(self,store_uuid):
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        month_start = today.strftime('%Y-%m') + "-01"
        return {
            'day': self.model.objects.filter(store__uuid=store_uuid,create_time__range=[today, tomorrow]).count(),
            'month':self.model.objects.filter(store__uuid=store_uuid,create_time__range=[month_start, tomorrow]).count(),
            'all':self.model.objects.filter(store__uuid=store_uuid).count(),
        }

if __name__ == '__main__':
    s = DBPrize()
    l = s.get_list()
    print (l)