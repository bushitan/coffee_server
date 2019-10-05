#coding:utf-8

from django.http import HttpResponse
import json
import lite.uitls.message as MSG
import json
import logging
logger = logging.getLogger("django") # 为loggers中定义的名称

from ..action_code import *

def logged(func):
    def wrapper(self,request,*args, **kwargs):
        try:
            # message,data = func(self,request,*args, **kwargs)
            result = func(self,request,*args, **kwargs)
            if('code' in result.keys()):

                _code = result['code']
            else:
                _code = CODE_SYS_SUCCESS

            if('data' in result.keys()):
                data = result['data']
            else:
                data = {}

            _dict = {
                'code':_code ,
                'message':code_to_message(_code) ,
                'data': data
            }
            # raise ("123")
            return HttpResponse( json.dumps( _dict ),content_type="application/json" )
        except Exception as e:
            logger.error(self.__class__.__name__ +" ---- " + str(e)) #打印错误日志
            _dict = {
                'code':CODE_SYS_ERROR,
                'message':MSG.sys_error() ,
                'class_name': self.__class__.__name__,
                'error':  str(e)
            }
            return HttpResponse( json.dumps( _dict ),content_type="application/json" )
    return wrapper
