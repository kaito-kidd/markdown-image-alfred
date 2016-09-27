# coding: utf8

"""上传文件到七牛云空间"""

__author__ = 'silverbulletkaito@gmail.com'

import os

from qiniu import Auth, put_file


def upload(path, access_key, secret_key, bucket_name):
    """上传文件到七牛云空间

    :param path: 文件路径
    """

    # 构建鉴权对象
    auth = Auth(access_key, secret_key)

    key = os.path.split(path)[-1]

    # 生成上传 Token，可以指定过期时间等
    token = auth.upload_token(bucket_name, key, 3600)

    ret, _ = put_file(token, key, path)

    return ret and ret['key'] == key

