#coding:utf-8
from uuid import uuid1

def short_uuid_create(uuid):
    uuidChars = ("a", "b", "c", "d", "e", "f",
             "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
             "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5",
             "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I",
             "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
             "W", "X", "Y", "Z")
    uuid = str(uuid).replace('-', '')
    result = ''
    for i in range(0,8):
        sub = uuid[i * 4: i * 4 + 4]
        x = int(sub,16)
        result += uuidChars[x % 0x3E]
    return str(result)



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