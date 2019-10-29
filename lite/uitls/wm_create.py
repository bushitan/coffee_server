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
                "width":300,
            }
            a._post_qr(token,data,qr_path)

    # 增加外卖门票
    # @param
    #   store_uuid 店铺uuid
    #   num 生成的数量
    def add_wm_ticket(self,store_uuid,num ,ticket_type ):
        return action_wm.add_ticket_list(store_uuid,num,ticket_type )


class WmUtils():
    def __init__(self):
        pass

    # 重新创建外卖对象
    def create(self,store_uuid,ticket_num ,ticket_type ):
        wc = WmCreate()
        # 增加ticket
        store_id,start,end = wc.add_wm_ticket(store_uuid,ticket_num,ticket_type )
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

    # store_uuid = '68e54718-7156-11e9-b456-e95aa2c51b5d' # 1 丰兄的店
    # store_uuid = '7d1dba9a-730b-11e9-9c73-e95aa2c51b5d' # 4 乐知咖啡
    # store_uuid = '54931e42-7c67-11e9-b94e-e95aa2c51b5d' # 17 白日梦想家
    # store_uuid = 'e12675ca-76df-11e9-8b6c-e95aa2c51b5d' # 8 愉市
    # store_uuid = 'a1828928-7860-11e9-be7b-e95aa2c51b5d' # 10 菓缇
    # store_uuid = '3a257d7e-9e3e-11e9-bacb-e95aa2c51b5d' # 22 又至园精品咖啡馆
    # store_uuid = 'b29c4dee-b35e-11e9-869d-e95aa2c51b5d' # 24 StrongCOFFEE(康浦店)
    # store_uuid = 'b131ffba-b362-11e9-9abd-e95aa2c51b5d' # 25 O.CT
    store_uuid = 'a85e7854-c268-11e9-97aa-e95aa2c51b5d' # 28 seeking
    # store_uuid = 'dfc006be-c0ca-11e9-9e96-e95aa2c51b5d' # 27 r-coffee
    # store_uuid = 'aa03edc2-ce62-11e9-afbe-e95aa2c51b5d' # 29 白鲸手作（广场东里店、和平路店）
    # store_uuid = 'afe5a7ba-d3ae-11e9-841f-e95aa2c51b5d' # 30 一城之肆
    # store_uuid = '381719ac-d499-11e9-95a1-e95aa2c51b5d' # 31 白鲸手作（贵兴店）
    # store_uuid = '7ecc8afa-d9ee-11e9-8590-e95aa2c51b5d' # 32 TJ
    # store_uuid = 'b5eb1a3e-dd39-11e9-b2c8-e95aa2c51b5d' # 34 2F Nail美甲美睫美颜
    # store_uuid = "3e5075ee-f2e5-11e9-8fd0-e95aa2c51b5d" # 35 The Knowhere Mixology
    # store_uuid = "001fc670-f4b3-11e9-aa2b-e95aa2c51b5d" # 36 FIGAS





    ticket_num = 12000  # 外卖券数量

    '''门票的类别，默认为积分模式 '''
    ticket_type = TICKET_TYPE_SCORE   #积分
    # ticket_type = TICKET_TYPE_SHARE 	#分享
    # ticket_type = TICKET_TYPE_DOUBLE 	#并行
    # ticket_type = TICKET_TYPE_CLOSE   #关闭

    # 创建新的外卖码
    # wm_utils.create(store_uuid,ticket_num ,ticket_type)

    # 根据序号重复生成
    wm_utils.save_image(28, 80601, 83000 )
    wm_utils.save_image(28, 83001, 85400 )
    wm_utils.save_image(28, 85401, 87800 )
    wm_utils.save_image(28, 87801, 90200 )
    wm_utils.save_image(28, 90201, 92600 )
    # wm_utils.save_image(28,56901,58100)
    # wm_utils.save_image(28,58101,59300)

    # wm_utils.save_image(28,,)


# mysql 查询重复
 # select  store_id  , id ,short_uuid , is_used  from `lite_wmticket` where short_uuid in  (
	# 	SELECT  short_uuid   FROM `lite_wmticket` GROUP BY binary short_uuid HAVING COUNT( binary short_uuid)>1
 #  ) and create_time>"2019-10-24"  order by store_id  , short_uuid desc





