# -*- coding:utf-8 -*-

# ======================================================================================================================
# ANIME DOWNLOAD
# AUTHOR: SUN
# DESCRIPTION: 网络图片的操作
# ======================================================================================================================

import os.path
from requests import get
from re import findall


def pic_download(url, path, name, fmat=None):
    # 图片下载
    if fmat is None:
        fmat = findall(r'(\..*)$', url)
        try:
            fmat = fmat[0]
        except IndexError:
            pass
    with open(os.path.join(path, name + fmat), 'wb') as p:
        response = get(url=url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        })
        p.write(response.content)
        p.close()


def pic_get(url):
    return get(url=url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }).content


if __name__ == '__main__':
    pass
