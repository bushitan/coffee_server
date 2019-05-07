#coding:utf-8

from django.http import HttpResponse
import json
import lite.uitls.message as MSG

def logged(func):
    def wrapper(self,request,*args, **kwargs):
        try:
        #     print ('1 call %s():' % self.__class__.__name__)
            message,data = func(self,request,*args, **kwargs)
            _dict = {
                # 'code':code,
                'message':message ,
                'data': data
            }
            return HttpResponse( json.dumps( _dict ),content_type="application/json" )
        except BaseException as e:
            _dict = {
                'class_name' : self.__class__.__name__,
                "error":str(e),
            }
            return HttpResponse( json.dumps( _dict ),content_type="application/json" )
    return wrapper
