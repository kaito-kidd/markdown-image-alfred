# 描述
复制本地图片或截图，快速上传图片到七牛云空间，并获取Markdown格式的图片地址。

# 功能

- 本地图片 --> Markdown图片链接
- 截图 --> Markdown图片链接
- gif格式 --> Markdown图片链接

# 快捷键

`option + command + v`

# 依赖

- 已注册好的七牛图床
- 付费版Alfred

# 使用

- 下载alfredworkflow文件，双击安装
- 复制本地一张图片(jpg,png,gif)或截一张图
- 打开任意编辑器，按下`option + command + v`快捷键
- 第一次操作需设置七牛的相关参数，会自动打开配置文件，填入配置即可
- 再次按下快捷键`option + command + v`后，自动插入上传后图片的图片链接

# 说明

插入的图片链接不是标准的Markdown格式，而是`img`标签<br/>
由于在retina屏幕下截图后，在非retina屏幕下图片会非常大，很难看<br/>
所以使用`img`标签的属性保证图片的大小和质量
