#coding:utf-8
class DB(object):
	def __init__(self,model = None):
		self.model = model

	# 列表转数组
	def _pack_list(self,_pack_fun,query_filter):
		_list = []
		for q in query_filter:
			_list.append( _pack_fun(q) )
		return _list
	# 对象转字典
	def _pack_dict(self,object):
		return {
			"name":object.name,
            "create_time":object.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "uuid":object.uuid,
		}

	def is_exists(self, *args, **kwargs):
		return self.model.objects.filter(*args, **kwargs).exists()

	def add(self,*args,**kwargs):
		_m = self.model(*args,**kwargs)
		_m.save()
		return self._pack_dict(_m)

	def get(self,*args,**kwargs):
		_m = self.model.objects.get(*args,**kwargs)
		return _m
	def filter(self,*args,**kwargs):
		_m = self.model.objects.filter(*args,**kwargs)
		return _m

	def last(self,*args,**kwargs):
		_m = self.model.objects.filter(*args,**kwargs).last()
		return _m

	def count(self,*args,**kwargs):
		# print (self.model.objects.filter(*args,**kwargs))
		_count = self.model.objects.filter(*args,**kwargs).count()
		return _count

	def get_dict(self,*args,**kwargs):
		_m = self.model.objects.get(*args,**kwargs)
		return self._pack_dict(_m)

	def get_list(self,*args,**kwargs):
		_m = self.model.objects.filter(*args,**kwargs)
		return self._pack_list( self._pack_dict,_m)

	# 获取一定范围内的数据
	def get_list_range(self,page_num,range,*args,**kwargs):
		start_index = page_num * range
		end_index = (page_num + 1)* range
		_m = self.model.objects.filter(*args,**kwargs)[start_index:end_index]
		return self._pack_list( self._pack_dict,_m)

	def update(self,model,*args,**kwargs):
		return model.update(*args,**kwargs)

	def delete(self,*args,**kwargs):
		_m = self.model.objects.filter(*args,**kwargs)
		_count = _m.count()
		_m.delete()
		return _count
		# _m.save()
		# return True


class DBUser(DB):
	def _pack_dict(self,object):
		_base = super()._pack_dict(object)
		_new = {
            "name":object.name,
            "create_time":object.create_time.strftime("%Y-%m-%d"),

            "uuid":object.uuid,
            "nick_name":object.nick_name,
            "avatar_url":object.avatar_url,
            "gender":object.gender,
            "city":object.city,
            "province":object.province,
            "country":object.country,

            "wx_openid":object.wx_openid,
            "wx_session":object.wx_session,
            "wx_unionid":object.wx_unionid,
		}
		return dict(_base,**_new)

class DBData(DB):
	def _pack_dict(self,object):
		_base = super()._pack_dict(object)
		_new = {
			"share_uuid":object.uuid,
			"store_id":object.store_id,
			"seller_id":object.seller_id,
			"customer_id":object.customer_id,
		 	"seller_avatar_url":object.seller.avatar_url if object.seller is not None else "" ,
            "seller_nick_name":object.seller.nick_name if object.seller is not None else "" ,

            "customer_avatar_url":object.customer.avatar_url if object.customer is not None else "" ,
            "customer_nick_name":object.customer.nick_name if object.customer is not None else "" ,
            "valid_time":object.valid_time.strftime("%Y-%m-%d %H:%M:%S"),
			"is_delete":object.is_delete,
		}
		return dict(_base,**_new)
	# def __init__(self):
	# 	super().__init__(Score)




