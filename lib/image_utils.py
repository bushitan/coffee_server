#coding:utf-8
from coffee_server.settings import *
import qiniu
# 七牛配置 -- 表情袋
qiniu_access_key = 'bK5xWj0a-TBIljlxHYOHuQib9HYF_9Ft-HtP8tEb'
qiniu_secret_key = '56lucORYc45sF5eDqNk63mLXsQ78n4RrubIrjtE0'
qiniu_bucket_name = 'clickz'

COFFEE_IMAGE_SPACE = 'coffee_image/upload'
class ImageUtils:
    def __init__(self):
        pass

    @staticmethod
    def rename(instance, filename):
        suffix = filename.split('.')[-1]
        key = '%s/%s.%s' %( COFFEE_IMAGE_SPACE,instance.short_uuid ,suffix)
        print ( os.path.isfile(MEDIA_ROOT+key))
        local_file = MEDIA_ROOT+key
        if os.path.isfile(local_file):
            os.remove(local_file)
        return key

    @staticmethod
    def put(key,local_file):
        q = qiniu.Auth(qiniu_access_key, qiniu_secret_key)
        token = q.upload_token(qiniu_bucket_name, key)
        ret, info = qiniu.put_file(token, key, local_file,check_crc=True)
        print (ret ,info)
        # return '/upload/'.join([MEDIA_ROOT, instance.short_uuid, filename])