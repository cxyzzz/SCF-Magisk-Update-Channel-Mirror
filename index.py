# -*- coding: utf-8 -*-

# github release 下载加速来源：https://jinfeijie.cn/post-805.html，禁止大文件下载，注意合理使用

import requests

magisk_channel_repo_url = 'https://cdn.jsdelivr.net/gh/topjohnwu/magisk_files@'


def raw_to_jsdelivr(url):
    str = url.split('/')
    author = str[3]
    repo = str[4]
    version = str[5]
    path = '/'.join(str[6:])
    return f'https://cdn.jsdelivr.net/gh/{author}/{repo}@{version}/{path}'


def main(event, context):
    print(event)
    channel_list = ('stable', 'beta', 'canary')
    args = event['queryString']
    channel = args.get('channel')
    if(channel not in channel_list):
        channel = 'stable'
    if(channel == 'canary'):
        channel = 'debug'
    if(channel in ('stable', 'beta')):
        branch = 'master'
    else:
        branch = 'canary'

    url = f'{magisk_channel_repo_url}{branch}/{channel}.json'
    response = requests.get(url)
    res = response.json()
    _res = res.copy()

    app = _res['app']
    uninstaller = _res['uninstaller']
    magisk = _res['magisk']
    stub = _res['stub']

    if(branch == 'master'):
        res['app']['link'] = app['link'].replace(
            'github.com', 'github.strcpy.cn')
        res['app']['note'] = raw_to_jsdelivr(app['note'])
        res['uninstaller']['link'] = uninstaller['link'].replace(
            'github.com', 'github.strcpy.cn')
        res['magisk']['link'] = magisk['link'].replace(
            'github.com', 'github.strcpy.cn')
        res['magisk']['note'] = raw_to_jsdelivr(magisk['note'])
        res['stub']['link'] = raw_to_jsdelivr(stub['link'])
    else:
        res['app']['link'] = raw_to_jsdelivr(app['link'])
        res['app']['note'] = raw_to_jsdelivr(app['note'])
        res['uninstaller']['link'] = raw_to_jsdelivr(uninstaller['link'])
        res['magisk']['link'] = raw_to_jsdelivr(magisk['link'])
        res['magisk']['note'] = raw_to_jsdelivr(magisk['note'])
        res['stub']['link'] = raw_to_jsdelivr(stub['link'])

    print(res)
    return(res)
