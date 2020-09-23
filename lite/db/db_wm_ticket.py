#coding:utf-8
from lite.db.db import DB
from lite.models import *
from django.db import transaction
import datetime
from django.db.models import Max

class DBWmTicket(DB):
    def __init__(self):
        super().__init__(WmTicket)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        _new = {
            "short_id":object.id,
            "short_uuid":object.short_uuid,
            "store_id":object.store_id,
            "store_title":object.store.title if object.store is not None else "",
            "is_used":object.is_used,
            "is_delete":object.is_delete,
            "start_time":object.start_time.strftime("%Y-%m-%d"),
            "end_time":object.end_time.strftime("%Y-%m-%d"),
        }
        return dict(_base,**_new)

    # 批量增加wm_ticket ，挨个保存生成short_uuid
    # @ param
    #   store 店铺
    #   num 生成的数量
    # @return
    #   文件名字 1_55_56
    def add_list(self,store,num,ticket_type):
        count = self.model.objects.all().aggregate(Max('id'))['id__max']
        # print (count )
        # return  store.id , count + 1 , count + num
        #
        # count = self.model.objects.count()

        index = self.model.objects.filter(store=store).count()
        name = "%s,%s" %( datetime.datetime.strftime( datetime.datetime.now(),'%Y_%m_%d_%H_%M_%S'),num )
        with transaction.atomic():
            for i in range(0,num):
                self.add(store=store, sn = index + 1 + i, name = name ,type = ticket_type) # 7.11版本
                # self.add(store=store, name = name) # 6.15版本 没有sn

        # return  "%s_%s_%s" %(store.id , count + 1 , count + num)
        return  store.id , count + 1 , count + num

    def get_by_short_uuid(self,short_uuid):
         return self.model.objects.extra(where=['short_uuid=%s'], params=[short_uuid]).first()

    '''
        @method 外卖券设置为已使用
        @param
            id：外卖券的id
            customer：使用的顾客对象
        @return 返回更新成功信息
    '''
    def set_used(self,id,customer):
        ticket = self.model.objects.get(id = id)
        ticket.is_used = True
        ticket.customer = customer
        ticket.save()
        return ticket

    '''
        @method 根据开-结束的范围，获取tikect的信息
        @param
            start 开始的序号
            end 结束的徐hao
        @return
            wm_list 外卖列表
    '''
    def get_start_end(self,start,end):
        ticket_filter = self.model.objects.filter(id__gte = start, id__lte = end)
        return self._pack_list(self._pack_dict,ticket_filter)



if __name__  == '__main__':
    import django
    django.setup()
    a= DBWmTicket()
    print ( a.get_by_short_uuid("MMIXf6fZ") )

    t =  a.get_by_short_uuid("MMIXf6fZ")
    print (t.id , t.is_used)
    # a.set_used(t.id)

    t =  a.get_by_short_uuid("MMIXf6fZ")
    print (t.id , t.is_used)


    # w = WmTicket.objects.extra(where=['binary short_uuid=%s'], params=["MMIXf6fZ"])
    # print(w)
    # a.get_dict(uuid = '	957a6946-63f8-11e9-8597-b83312f00bac')
    # print (a.get_dict(id = 1 ))
    # print (a.get_dict(uuid = '957a6946-63f8-11e9-8597-b83312f00bac' ))
    # print (a.update( a.filter(id=3),store_id = 1 ))