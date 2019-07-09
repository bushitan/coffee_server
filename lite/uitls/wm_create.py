#coding:utf-8

from lite.db.db_wm_ticket import *
from lite.action.action_user import *
action_customer = ActionCustomer()
from lite.action.action_wm import *
action_wm = ActionWm()
from lite.action.action_qr import *
from lite.db.db_store import *
import time
import os

class WmCreate:
    def __init__(self):
        self.db_store = DBStore()
        self.db_wm_ticket = DBWmTicket()
        self.base_path = r"C:\server\coffee_image\wm\\"

    # 新版本
    # 自定义外卖二维码存放地址
    # @param
    #   file_path 文件夹地址
    def create_file_path(self,file_path):
        if  os.path.exists(file_path) is False:
            os.makedirs(file_path)
            return file_path
        else :
            return False

    # 按范围查询外卖券
    # @param
    #   start 开始位置
    #   end 结束位置
    def query_ticket(self ,start ,end):
        return  self.db_wm_ticket.filter(id__gte = start, id__lte = end)

    # 根据文档地址，开始结束范围，请求二维码
    # @param
    #   file_path 保存的文件夹位置
    #   ticket_list 外卖券数组
    def add_qr_in_file(self,file_path,ticket_list):
        # 初始化二维码列表
        a = ActionQR("wxd19bbe9cb3b293b6", "931ad8364ea6a1327ed65282af330415") # 分享积点卡客户端
        token = a.get_access_token() # 获取token

        for t in ticket_list:
            short_uuid = t.short_uuid
            # qr_path = file_path + "wm_%s_%s.png" %(t.id ,short_uuid )
            qr_path = file_path + "%s.png" %(t.id  )  #  文件命名
            data = {
                "scene":"wm_%s" % (short_uuid),
                "is_hyaline" :True,
            }
            a._post_qr(token,data,qr_path)

    # 增加外卖门票
    # @param
    #   store_uuid 店铺uuid
    #   num 生成的数量
    def add_wm_ticket(self,store_uuid,num  ):
        return action_wm.add_ticket_list(store_uuid,num )


class WmUtils():
    def __init__(self):
        pass

    # 重新创建外卖对象
    def create(self,store_uuid,ticket_num  ):
        wc = WmCreate()
        # 增加ticket
        store_id,start,end = wc.add_wm_ticket(store_uuid,ticket_num )
        # 保存图片
        self.save_image(store_id,start,end)

    # 再已经有的基础上，重新生成二维码。
    def save_image(self,store_id,start,end):
        wc = WmCreate()
        # 创建文件夹
        file_path = wc.base_path + "%s_%s_%s\\" %(store_id , start , end)
        wc.create_file_path(file_path)
        # 查询数组
        ticket_list = wc.query_ticket(start,end)
        # 请求保存二维码
        wc.add_qr_in_file(file_path,ticket_list)



if __name__  == '__main__':
    import django
    django.setup()
    wm_utils = WmUtils()

    # store_uuid = '68e54718-7156-11e9-b456-e95aa2c51b5d' # 丰胸的点
    store_uuid = '54931e42-7c67-11e9-b94e-e95aa2c51b5d' # 17 白日梦想家
    ticket_num = 2 # 外卖券数量
    # sn_tag = u"2017_07_09_2"
    num = ticket_num

    # print ( "%s,%s" %( datetime.datetime.strftime( datetime.datetime.now(),'%Y_%m_%d_%H_%M_%S'),num ) )
    # 重新创建
    wm_utils.create(store_uuid,ticket_num )

    # 再次生成
    # store_id  , start , end
    # wm_utils.save_image(17,501,1700)