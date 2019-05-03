#coding:utf-8

class InfoMap():
    def __init__(self):
        self.info_map = {}
        pass
    def add(self,key,value):
        _value =  self.info_map.get(key,None)
        if _value is None:
            self.info_map[key] = [value]
        else:
            self.info_map[key].append(value)
        return True

    def get_map(self):
        return self.info_map

    def pop(self,key):
        value = self.info_map.pop(key,None)
        return value
        # return value
        # if value is None :
        #     return { 'message':u'none'}
        # else:
        #     return {'value':value}

# if __name__ == "__main__":
#     map = {'78ba8814-6c0b-11e9-9b35-b83312f00bac': [{'title': '分享好友成功', 'code': '104001', 'content': '获得了1点'}]}
#     key = '78ba8814-6c0b-11e9-9b35-b83312f00bac'
#     print (map.pop(key,None))
#     print ( map)
#
#     info_map = InfoMap()
#     info_map.add(
#          '78ba8814-6c0b-11e9-9b35-b83312f00bac',
#          {'content': '获得了1点', 'code': '104001', 'title': '分享好友成功'}
#      )
#     print (info_map.pop(key))