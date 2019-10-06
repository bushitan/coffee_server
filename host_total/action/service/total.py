#coding:utf-8
from host_total.action.action_base import ActionBase
# from ..action_code import *
# from host_total.db.db_utils import db_utils
from coffee_server.settings import *
from host_total.db.db_utils import db_utils

'''
    @class 业务权限检测
'''
class ActionTotal(ActionBase):
    def __init__(self):
        super().__init__()
    def test(self):
        pass
        print (db_utils.seller.filter(uuid='1bb68822-7156-11e9-902f-e95aa2c51b5d'))

    # 1.1 检测账号是否存在
    def check_account(self,username,password):
        return db_utils.seller.is_exists( username=username,password=password )
        # return db_utils.seller.is_exists( id=1 )

    # 1.2 获取用户信息
    def get_seller_info(self,username,password):
        return db_utils.seller.get_dict( username=username,password=password )
        # return db_utils.seller.get_dict(  id=1 )

    # 1.3 检查token是否存在
    def check_token(self,token):
        return db_utils.seller.is_exists( wx_session=token)


    # 2.1 获取门店数据
    def get_store_info(self,store_uuid):
        return db_utils.store.get_dict( uuid=store_uuid)

    # 2.1 获取综合统计数据
    def get_total(self,store_uuid):
        # store = db_utils.store.get( uuid=store_uuid)
        score_statistic = db_utils.score.get_statistic(store_uuid)
        prize_statistic = db_utils.prize.get_statistic(store_uuid)
        return {
            'day':{'score':score_statistic['day'],'prize':prize_statistic['day']},
            'month':{'score':score_statistic['month'],'prize':prize_statistic['month']},
            'all':{'score':score_statistic['all'],'prize':prize_statistic['all']},
        }

    # 2.2获取今天集点的坐标点
    def get_map(self,store_uuid):
        # store = db_utils.store.get( id=store_id)
        return db_utils.score.get_today(store_uuid)

    # 2.3 获取该店铺的所有核销员
    def get_seller_list(self,store_uuid):
        return db_utils.seller.get_list(store__uuid = store_uuid)

    # 3 获取核销员核销的积分详情
    def get_score_by_seller(self,seller_id,index,range):
        return db_utils.score.get_list(seller_id = seller_id)[index:range]


if __name__ == "__main__":
    import django
    django.setup()
    a = ActionTotal()
    # a.test()
    username = 'sa'
    password = "sa"

    # print (a.check_account(username,password))
    # print (a.get_seller_info(username,password))
    # print (a.check_token(token='TgkwmYj8qSxYXVz86Aeyng=='))
    # print (a.get_total(store_id=1))
    # print (a.get_seller_list(store_id=1))
    # print (  a.get_score_by_seller(1,0,10))
    # print (db_utils.store.get(id=1))

    # TODO 检测账号密码是否有
    # TODO 1、商户端加上账号和密码。

    # print (db_utils.seller.filter(uuid='1bb68822-7156-11e9-902f-e95aa2c51b5d'))
