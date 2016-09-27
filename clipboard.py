# coding: utf8

"""处理剪贴板相关的文件"""

__author__ = 'silverbulletkaito@gmail.com'

import os
import time

from AppKit import (
    NSPasteboard, NSFilenamesPboardType, NSPasteboardTypePNG,
    NSPasteboardTypeTIFF, NSPasteboardTypeString
)

class WriteFileError(Exception):
    """写入文件错误"""

    def __init__(self, file_type):
        super(WriteFileError, self).__init__(
            '写入{}文件异常!'.format(file_type))


class FileTypeUnsupportedError(Exception):
    """上传的文件类型不支持"""

    def __init__(self, file_type):
        super(FileTypeUnsupportedError, self).__init__(
            '不支持的文件类型:{}!'.format(file_type))


class NotImageError(Exception):
    """不是图片错误"""

    def __init__(self):
        super(NotImageError, self).__init__(
            '请复制图片或截图再进行操作!')


# 只支持上传的图片文件格式
ALLOW_FILE_TYPES = ('png', 'jpeg', 'jpg', 'gif', 'tiff')

TYPE_MAP = {
    'png': NSPasteboardTypePNG,
    'tiff': NSPasteboardTypeTIFF,
}


def get_pasteboard_file_path():
    """获取剪贴板的文件路径"""

    # 获取系统剪贴板对象
    pasteboard = NSPasteboard.generalPasteboard()
    # 剪贴板里的数据类型
    data_type = pasteboard.types()

    # 如果是直接复制的文件
    if NSFilenamesPboardType in data_type:
        # 获取到这个文件的路径和类型
        file_path = pasteboard.propertyListForType_(NSFilenamesPboardType)[0]
        return file_path

    now = int(time.time())

    # 剪贴板是png,tiff文件,生成文件返回文件路径
    for file_type, pastedboard_file_type in TYPE_MAP.items():
        if pastedboard_file_type not in data_type:
            continue
        filename = '{}.{}'.format(now, file_type)
        file_path = '/tmp/%s' % filename

        data = pasteboard.dataForType_(pastedboard_file_type)
        ret = data.writeToFile_atomically_(file_path, False)
        if not ret:
            raise WriteFileError(file_type)
        return file_path


def get_pasteboard_img_path():
    """获取剪贴板图片文件路径"""

    file_path = get_pasteboard_file_path()
    if not file_path:
        raise NotImageError()

    file_name = os.path.split(file_path)[-1]
    file_type = file_name.split('.')[-1]

    # 检查是否是图片类型的文件
    if file_type not in ALLOW_FILE_TYPES:
        raise FileTypeUnsupportedError(file_type)

    return file_path
