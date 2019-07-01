#coding:utf-8
from lite.db.db import DBUser
from lite.models import *


class DBSeller(DBUser):
    def __init__(self):
        super().__init__(Seller)

    # 基础的查询数据
    def _pack_dict(self,object):
        _base = super()._pack_dict(object)
        _new = {
            "is_host":object.is_host,
            "store_uuid":object.store.uuid if object.store is not None else "" ,
        }
        return dict(_base,**_new)

if __name__  == '__main__':
    import django
    django.setup()
    s= DBSeller()
    # a.get_dict(uuid = '	957a6946-63f8-11e9-8597-b83312f00bac')
    # print (a.get_dict(id = 1 ))
    # print (a.get_dict(uuid = '1bb68822-7156-11e9-902f-e95aa2c51b5d' ))

    # seller = s.get(id = 1)
    # print(seller)
    # print (u"\\xF0\\x9F\\x98\\x88")
    # seller.name = u"\\xF0\\x9F\\x98\\x88"
    # seller.save()
    # import base64
    # nick_name = "this.丰兄"
    # encodestr = base64.b64encode(nick_name.encode('utf-8'))
    # print(str(encodestr,'utf-8'))
    #
    # str(base64.b64encode(nick_name.encode('utf-8')),'utf-8')
    #
    #
    # d =  base64.b64decode(encodestr)
    #
    # # print( base64.b64decode(encodestr))
    # print( str(base64.b64decode(encodestr),'utf-8')   )
    # print (a.update( a.filter(id=3),store_id = 1 ))

