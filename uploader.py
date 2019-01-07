# coding: utf8

"""上传文件到七牛云空间"""

__author__ = 'silverbulletkaito@gmail.com'

import os
import time

from qiniu import Auth, put_file


def upload(path, access_key, secret_key, bucket_name, uri_prefix):
    """上传文件到七牛云空间

    :param path: 文件路径
    """

    # 构建鉴权对象
    auth = Auth(access_key, secret_key)

    # 上传到七牛后保存的文件名
    old_file_name = os.path.split(path)[-1]
    suffix = old_file_name.split('.')[-1]
    key = '{}.{}'.format(int(time.time()), suffix)

    # 生成上传 Token，可以指定过期时间等
    token = auth.upload_token(bucket_name, key, 3600)

    ret, _ = put_file(token, key, path)

    if ret and ret['key'] == key:
        return os.path.join(uri_prefix, key)
    else:
        return None

    # return ret and ret['key'] == key

