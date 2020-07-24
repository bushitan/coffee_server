# #coding:utf-8
# # from django.urls import resolve, reverse
# from django.test import TestCase
# from coffee_server.settings import ENV_URL
# import json
#
# APP = "lite/"
# class Demo(TestCase):
#     fixtures = ['mysql.json']
#
#     def setUp(self):
#         # print('setUp')
#         self.name = 'Django'
#
#     # def test_heelow_test_case(self):
#     #     print('test_heelow')
#
#
#     # def test_hello_test_case(self):
#     #     url = '/' + ENV_URL + 'photo/base/login/'
#     #     response = self.client.post(url)
#     #     self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
#     #
#     #     data = json.loads(str(response.content,'utf-8'))
#     #     print ('test_hello_test_case',data)
#     #     self.assertEqual(data['message']['code'], '200001')  # 期望的msg返回结果为'Hello , I am a test Case'
#
#     '''
#         @method 系统更新用户信息
#     '''
#     def test_sys_set_user_info(self):
#         url = '/' + ENV_URL + APP + 'scan/wm/customer/'
#         data = {
#             "uuid":'1cff3e06-adf7-11e9-b8ce-e95aa2c51b5d', #丰兄
#             'nickName':'this.丰兄 (¦(¦',
#             'avatarUrl':'21321',
#             'gender':'',
#             'city':'',
#             'province':'',
#             'country':'',
#         }
#         response = self.client.post(url,data = data)
#         self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
#         data = json.loads(str(response.content,'utf-8'))
#         print ('test_sys_set_user_info',data)
#
#
#     '''
#         @method 查询文章详情
#     '''
#     def test_article_get_list(self):
#         url = '/' + ENV_URL + APP + 'article/get/list/'
#         response = self.client.post(url)
#         self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
#         data = json.loads(str(response.content,'utf-8'))
#         print ('test_article_get_detail',data)
#
#
#
#
#     # def tearDown(self):
#         # print('tearDown')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #coding:utf-8
# from django.test import TestCase
#
# from lib.info_map import *
# info_map = InfoMap()
# print (info_map)
# info_map.add('aa',{ 'message':'1234' })
# info_map.add('aa',{ 'message':'1234' })
# print (info_map.get_map())
#
# print (info_map.pop('aa'))
# print (info_map.get_map())
# print (info_map.pop('aa'))
# print (info_map.get_map())
#
# # import requests
# # url = 'https://www.xiaohongshu.com/discovery/item/5d25f0f8000000002701243f'
# # headers = {'content-type': 'application/json'}
# # r = requests.get(url, headers=headers )
# # print(r)
# # f=open('red.html',"wb")
# # f.write(r.content)
# # f.close()
# # Create your tests here.
# # INFO_QUEUE = {}
# # INFO_QUEUE['aa'] = [ {'message':'me'}, {'message':'u1'},]
# # INFO_QUEUE['bb'] = [ {'message':'me123'}, {'message':'1123'},]
# #
# # def get_value(key):
# #     value = INFO_QUEUE.pop(key,None)
# #     if value is None :
# #         return { 'message':u'none'}
# #     else:
# #         return {'value':value}
# # key = 'aa'
# # v = get_value(key)
# # print (v)
# # print (INFO_QUEUE)