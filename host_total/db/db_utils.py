#coding:utf-8
#
# from photo.db.db_article import *
# from photo.db.db_gallery import *
# from photo.db.db_prize import *
# from photo.db.db_score import *
# from photo.db.db_store import *
# from photo.db.db_tag import *
# from photo.db.db_user import *
# from photo.db.db_base_image import *
from host_total.db.db_store import *
from host_total.db.db_score import *
from host_total.db.db_prize import *
from host_total.db.db_seller import *



class DBUtils():
    # article = 1
    def __init__(self):
        # self.ad = DBAd()

        self.store = DBStore()
        self.score = DBScore()
        self.prize = DBPrize()
        self.seller = DBSeller()


        # self.prize = DBPrize()
        # self.score = DBScore()
        # self.store = DBStore()
        # self.tag = DBTag()
        # self.user = DBUser()
        # self.base_image = DBBaseImage()
        # self.like = DBLike()
db_utils = DBUtils()

if __name__ == "__main__":
    import django
    django.setup()
    db_utils = DBUtils()
    # print (db_utils.store.get(id=1))

    # TODO 检测账号密码是否有
    # TODO 1、商户端加上账号和密码。

    print (db_utils.seller.filter(uuid='1bb68822-7156-11e9-902f-e95aa2c51b5d'))

    # print (db.article.all())
    # print (db.article.is_exists(id = 2 ))


