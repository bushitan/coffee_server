#coding:utf-8
from weixin import WeixinLogin
from lite.action.action_user import ActionUser
import requests
import time
import json

# 销售者的动作
class ActionQR(ActionUser):
    def __init__(self,app_id,app_secret):
        self.app_id = app_id
        self.app_secret = app_secret
        self.ACCESS_TOKEN = {'access_token':"",'expires_in':7200,'valid_unix':0}
        self.wxLogin = WeixinLogin(app_id, app_secret)
           # 根据js_code获取session
    def checkSession(self,code,uuid):
        # print code,user_id
        if uuid == "" or self.db_user.is_exists(uuid = uuid) is False:
            print (code , uuid)
            data = self.wxLogin.jscode2session(code) # self.getLogin(app_id,code)
            print (data)
            return self._checkUser(data) # 新用户存入
        return self.db_user.get_dict(uuid = uuid)
    # 获取外卖二维码
    def get_wm_qr(self,access_token ,data):
        file_name = data["scene"] + ".jpg" #按照sence，生成菊花码图片文件
        file_path = "C:/server/coffee_image/wm/" + file_name
        self._post_qr(access_token ,data,file_path)
        return file_name

    def get_qr(self,access_token ,data , file_path):
        file_name = data["scene"] + ".jpg" #按照sence，生成菊花码图片文件
        # file_path = path + file_name
        self._post_qr(access_token ,data,file_path)
        return file_name

    def _post_qr(self,access_token ,data,file_path):
        url = 'https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token=%s' % (access_token)
        headers = {'content-type': 'application/json'}
        r = requests.post(url,data=json.dumps(data), headers=headers )
        f=open(file_path,"wb")
        f.write(r.content)
        f.close()
        return True

    def post_wxacode(self,access_token ,data,file_path):
        url = 'https://api.weixin.qq.com/wxa/getwxacode?access_token=%s' % (access_token)
        headers = {'content-type': 'application/json'}
        r = requests.post(url,data=json.dumps(data), headers=headers )
        f=open(file_path,"wb")
        f.write(r.content)
        f.close()
        return True

    # 获取token
    def get_access_token(self):
        # print ('in token ', self.ACCESS_TOKEN)
        current_unix = time.time()
        if current_unix > self.ACCESS_TOKEN['valid_unix']:
            self._update_token()
        # print ('out token ',self.ACCESS_TOKEN)
        return self.ACCESS_TOKEN['access_token']

    # 更新touken
    def _update_token(self):
        expires_in = 7000
        current_unix = time.time()
        valid_unix = current_unix + expires_in
        _res = self._weixin_token()
        _res['valid_unix'] = valid_unix
        self.ACCESS_TOKEN = _res
        return  _res
    # 请求token
    def _weixin_token(self):
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (self.app_id , self.app_secret)
        r = requests.get(url)
        return json.loads( r.text)

if __name__  == '__main__':
    def map():
        a = ActionQR("wxd2f409241725502b", "986104a41ccaa0a5c25c253010277c56")
        token = a.get_access_token()
        file_path = "C:/server/coffee_image/map/34.png"
        data = {
            "path":"pages/route/route?mode=poi&poi_id=34",
            "is_hyaline" :True,
        }
        a.post_wxacode(token,data,file_path)

    def cus():

        a = ActionQR("wxd19bbe9cb3b293b6", "931ad8364ea6a1327ed65282af330415")
        token = a.get_access_token()
        file_path = "C:/server/coffee_image/map/wm.png"
        data = {
            "scene":"wm_2UdX86fZ",
            "is_hyaline" :True,
        }
        a._post_qr(token,data,file_path)
    map()
    # cus()