#coding:utf-8
from django.test import TestCase

from lib.info_map import *
info_map = InfoMap()
print (info_map)
info_map.add('aa',{ 'message':'1234' })
info_map.add('aa',{ 'message':'1234' })
print (info_map.get_map())

print (info_map.pop('aa'))
print (info_map.get_map())
print (info_map.pop('aa'))
print (info_map.get_map())
# Create your tests here.
# INFO_QUEUE = {}
# INFO_QUEUE['aa'] = [ {'message':'me'}, {'message':'u1'},]
# INFO_QUEUE['bb'] = [ {'message':'me123'}, {'message':'1123'},]
#
# def get_value(key):
#     value = INFO_QUEUE.pop(key,None)
#     if value is None :
#         return { 'message':u'none'}
#     else:
#         return {'value':value}
# key = 'aa'
# v = get_value(key)
# print (v)
# print (INFO_QUEUE)