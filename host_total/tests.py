#coding:utf-8
# from django.urls import resolve, reverse

#安装mysql

from django.test import TestCase
from coffee_server.settings import ENV_URL
import json
from .action.action_code import *

APP = "host_total/"
class Demo(TestCase):
    fixtures = ['mysql.json']

    def setUp(self):
        # print('setUp')
        self.name = 'Django'

    # def test_heelow_test_case(self):
    #     print('test_heelow')


    # def test_hello_test_case(self):
    #     url = '/' + ENV_URL + 'photo/base/login/'
    #     response = self.client.post(url)
    #     self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
    #
    #     data = json.loads(str(response.content,'utf-8'))
    #     print ('test_hello_test_case',data)
    #     self.assertEqual(data['message']['code'], '200001')  # 期望的msg返回结果为'Hello , I am a test Case'

    '''
        @method 系统更新用户信息
    '''
    def test_login(self):
        url = '/' + ENV_URL + APP + 'login/'
        # data = {
        #     # "username":'1cff3e06-adf7-11e9-b8ce-e95aa2c51b5d', #丰兄
        #     # 'password':'this.丰兄 (¦(¦',
        #     "username":'321', #丰兄
        #     'password':'1',
        # }
        # response = self.client.post(url,data = data)
        # self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
        # data = json.loads(str(response.content,'utf-8'))
        # print ('test_sys_set_user_info',data)

        data = {
            "username":'1', #丰兄
            'password':'1',
        }
        response = self.client.post(url,data = data)
        self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200

        data = json.loads(str(response.content,'utf-8'))
        self.assertEqual(data['code'], CODE_SERVICES_LOGIN_NONE)
        # self.assertEqual(data['code'], CODE_SYS_ERROR)

        # if (data['code'] == '101001'):
        #     print True

        # print ('test_sys_set_user_info',data)

    '''
        @method 2 综合统计数据
    '''
    def test_total(self):
        url = '/' + ENV_URL + APP + 'host_total/'
        data = {
            "store_id":'',
        }
        response = self.client.post(url,data = data)
        data = json.loads(str(response.content,'utf-8'))
        self.assertEqual(data['code'], 123)

    '''
        @method 3 集点地图
    '''
    def test_map(self):
        url = '/' + ENV_URL + APP + 'map/'
        data = {
            "store_id":'',
        }
        response = self.client.post(url,data = data)
        data = json.loads(str(response.content,'utf-8'))
        self.assertEqual(data['code'], 123)

    '''
        @method 4 销售组列表
    '''
    def test_seller_list(self):
        url = '/' + ENV_URL + APP + 'seller/list/'
        data = {
            "store_id":'',
        }
        response = self.client.post(url,data = data)
        data = json.loads(str(response.content,'utf-8'))
        self.assertEqual(data['code'], 123)

    '''
        @method 5 销售详情
    '''
    def test_seller_detail(self):
        url = '/' + ENV_URL + APP + 'seller/detail/'
        data = {
            "store_id":'',
        }
        response = self.client.post(url,data = data)
        data = json.loads(str(response.content,'utf-8'))
        self.assertEqual(data['code'], 123)