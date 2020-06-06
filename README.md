# SCF-Magisk-Update-Channel-Mirror
使用腾讯云函数处理Magisk更新通道数据，替换文件下载地址为Jsdelivr和https://jinfeijie.cn/post-805.html加速下载

## 使用方法
下载仓库压缩包，去腾讯云函数函数服务新建函数，函数名字任意，运行环境选择 Python3.6，创建方式选择空白函数，点击下一步将执行改为`index.main`，提交方法选择本地上传 ZIP 文件，然后点击高级设置，内存可以改为 64MB（节约免费额度，也可以不改），超时时间改为 60 秒，点击完成就部署好了。部署完成后点击触发管理创建触发器，选择API网关触发器，提交即可，创建好后会有一个地址，复制这个地址填入 Magisk Manager 自定义通道。可通过添加`channel=<xxx>`参数指定通道，默认为稳定通道，可选`stable`, `beta`, `canary`, `debug`，eg: https://xxx.pigw.tencentcs.com/test/magisk_channel_mirror?channel=debug。
