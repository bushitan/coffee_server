#coding:utf-8

from django.http import HttpResponse
import json
import lite.uitls.message as MSG
import json
import logging
import time
logger = logging.getLogger("django") # 为loggers中定义的名称

def logged(func):
    def wrapper(self,request,*args, **kwargs):
        try:

            time1 = time.time()
            message,data = func(self,request,*args, **kwargs)
            _dict = {
                # 'code':code,
                'message':message ,
                'data': data
            }
            print('1 log',  time.time()-time1)
            # raise ("123")
            return HttpResponse( json.dumps( _dict ),content_type="application/json" )
        except Exception as e:
            logger.error(self.__class__.__name__ +" ---- " + str(e)) #打印错误日志
            _dict = {
                'message':MSG.sys_error() ,
                'class_name': self.__class__.__name__,
                'error':  str(e)
            }
            return HttpResponse( json.dumps( _dict ),content_type="application/json" )
    return wrapper


