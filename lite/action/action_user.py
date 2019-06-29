#coding:utf-8
from weixin import WeixinLogin
from lite.db.db_customer import *
from lite.db.db_seller import *
import requests
import time
import json
import base64

import urllib
import urllib.request
from urllib import parse, request

class ActionUser():
	def __init__(self,model,app_id,app_secret):
		self.db_user = model()
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

	# 获取不受限制的菊花吗
	def get_un_limit_qr(self,access_token ,data):

		file_name = data["scene"] + ".jpg" #按照sence，生成菊花码图片文件
		file_path = "C:\server\wxacodeunlimit/" + file_name
		self._post_qr(access_token ,data,file_path)
		return file_name

	# 获取外卖二维码
	def get_wm_qr(self,access_token ,data):
		file_name = data["scene"] + ".jpg" #按照sence，生成菊花码图片文件
		file_path = "C:/server/coffee_image/wm/" + file_name
		self._post_qr(access_token ,data,file_path)
		return file_name
		# url = 'https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token=%s' % (access_token)
		# headers = {'content-type': 'application/json'}
		# r = requests.post(url,data=json.dumps(data), headers=headers )

		## file_name = "aa1a.jpg"
		# file_name = data["scene"] + ".jpg" #按照sence，生成菊花码图片文件
		# file_path = "C:\server\wxacodeunlimit/" + file_name
		# f=open(file_path,"wb")
		# f.write(r.content)
		# f.close()
		# return file_name

	def _post_qr(self,access_token ,data,file_path):
		url = 'https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token=%s' % (access_token)
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



	# 请求token
	def _weixin_token(self):
		url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (self.app_id , self.app_secret)
		r = requests.get(url)
		return json.loads( r.text)
		# print (int(t))
		# print(r.text)

	# 获取登陆信息
	# def getLogin(self,app_id,code):
	# 	if app_id == AII_ID_ZHAO_DD:
	# 		return login_zhaodd.jscode2session(code)
	# 	if app_id == AII_ID_COFFEE:
	# 		return login_coffee.jscode2session(code)
	# 	raise( 'APP_ID is null')

	# 检测用户是否存在
	def _checkUser(self,data):
		open_id = data['openid']
		session_key = data['session_key']
		# unionid = data['unionid']

		if self.db_user.is_exists(wx_openid = open_id) is True: #用户已存在，查询
			return self.db_user.get_dict(wx_openid = open_id)
		else: # 用户不存在，新增
			return self.db_user.add(
				wx_openid = open_id,
				wx_session = session_key,
				# wx_unionid = unionid,
			)

	# 更新用户信息
	def update_user_info(self,uuid,*args, **kwargs):
		user = self.db_user.filter(uuid = uuid)
		count = self.db_user.update(user,*args, **kwargs)
		return count

# 销售者的动作
class ActionSeller(ActionUser):
	def __init__(self):
		super().__init__(DBSeller,'wx3e0f68d227f05241','992415e91d1a96d539dec4ab13e5d90d')
		# self.db_user = model()

# 客户的动作
class ActionCustomer(ActionUser):
	def __init__(self):
		super().__init__(DBCustomer,'wxd19bbe9cb3b293b6','931ad8364ea6a1327ed65282af330415')


if __name__  == '__main__':
	a= ActionCustomer()
	# a.checkSession('011m3Wv42jb4IP0QRFy42cW0w42m3Wvu','')

	# str(b'123', encoding='utf-8')
	# a = bytes.decode(b'123')
	# print (a)
	# a.get_access_token()
	data = {
            "scene":"sdfghjkl",
            "page":"pages/route/route",
        }
	a.get_un_limit_qr("22_yZ9oeDbaM5z_G7-b7-0LPX1ahrcQAsoX4qntnBcAUYUU3yZqBHbTgqxNwY50xQ-yYYFb6K-Ob7FLwN_pKFAWZQ_rJuhOtk-2cjTJf3xju_js8jcbTX6YX1T9C_DvwJxmIaaAXEsfWO8ImVdiUEYhAAAAKE"
					  ,data)