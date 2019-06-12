#coding:utf-8

from django.http import HttpResponse
import json
import lite.uitls.message as MSG
import json
import logging
logger = logging.getLogger("django") # 为loggers中定义的名称

def logged(func):
    def wrapper(self,request,*args, **kwargs):
        try:
            message,data = func(self,request,*args, **kwargs)
            _dict = {
                # 'code':code,
                'message':message ,
                'data': data
            }
            return HttpResponse( json.dumps( _dict ),content_type="application/json" )
        except BaseException as e:
            logger.error(self.__class__.__name__ +" ---- " + str(e)) #打印错误日志
            _dict = {
                'message':MSG.sys_error() ,
                'class_name': self.__class__.__name__,
                'error':  str(e)
            }
            return HttpResponse( json.dumps( _dict ),content_type="application/json" )
    return wrapper
