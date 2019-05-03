#coding:utf-8
from weixin import WeixinLogin
from lite.db.db_customer import *
from lite.db.db_seller import *

class ActionUser():
	def __init__(self,model,app_id,app_secret):
		self.db_user = model()
		self.wxLogin = WeixinLogin(app_id, app_secret)

	def checkSession(self,code,uuid):
		# print code,user_id
		if uuid == "" or self.db_user.is_exists(uuid = uuid) is False:
			print (code , uuid)
			data = self.wxLogin.jscode2session(code) # self.getLogin(app_id,code)
			print (data)
			return self._checkUser(data) # 新用户存入
		return self.db_user.get_dict(uuid = uuid)

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
	a.checkSession('011m3Wv42jb4IP0QRFy42cW0w42m3Wvu','')