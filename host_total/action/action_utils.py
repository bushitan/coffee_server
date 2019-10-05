#coding:utf-8
from host_total.action.base.detection import *
from host_total.action.base.logger import *
from host_total.action.service.total import *

class ActionUtils():
    def __init__(self):
        self.detect = ActionDetect()
        self.logged = logged
        self.total = ActionTotal()

        # self.user = ActionUser()
        # self.article = ActionArticle()
action = ActionUtils()

if __name__ == "__main__":
    print ( action.detect.get_article_list())