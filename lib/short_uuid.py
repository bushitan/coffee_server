#coding:utf-8
from uuid import uuid1

from datetime import datetime
import time
def short_uuid_create(store_id,self_id):
    time.sleep(0.01)
    now = datetime.now().timestamp() # 获取当前datetime
    time.sleep(0.01)
    return "%s-%s-%s" % (store_id,self_id,now)


# def short_uuid_create(uuid):
#     uuidChars = ("a", "b", "c", "d", "e", "f",
#              "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
#              "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5",
#              "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I",
#              "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
#              "W", "X", "Y", "Z")
#     uuid = str(uuid).replace('-', '')
#     result = ''
#     for i in range(0,8):
#         sub = uuid[i * 4: i * 4 + 4]
#         x = int(sub,16)
#         result += uuidChars[x % 0x3E]
#     return str(result)
#
# print( short_uuid_create("ce109a42-ef1d-11e9-8c7c-e95aa2c51b5d") )
# print( short_uuid_create("98c8a430-f3b7-11e9-b10e-e95aa2c51b5d") )
# print( short_uuid_create("98c8a434-f3b7-11e9-b10e-e95aa2c51b5d") )



# def short_uuid_create():
#     uuidChars = ("a", "b", "c", "d", "e", "f",
#              "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
#              "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5",
#              "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I",
#              "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
#              "W", "X", "Y", "Z")
#     uuid = str(uuid1()).replace('-', '')
#     result = ''
#     for i in range(0,8):
#         sub = uuid[i * 4: i * 4 + 4]
#         x = int(sub,16)
#         result += uuidChars[x % 0x3E]
#     return result
# print(short_uuid_create())
# print(short_uuid_create())
# print(short_uuid_create())