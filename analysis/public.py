# -*- coding:utf-8 -*-

# ======================================================================================================================
# ANIME DOWNLOAD
# AUTHOR: SUN
# DESCRIPTION: 其他函数
# ======================================================================================================================

# model
"""
from bs4 import BeautifulSoup
from analysis import other
from broswer import add
import re

base = {
    'home_url': there,
    'research_url': there
}


def research(name):
    return add(
        url=base['research_url'] % other.url_change(name),
        xpath='/html/body/div[4]/div[2]',
        other=[there, 'research']
    )


def detail(url):
    return add(
        url=url,
        xpath=there,
        other=[there, 'detail'],
        timeout=15
    )


def research_analysis(html):
    soup = BeautifulSoup(html, 'lxml')
    result = []
    there
    result.append({
            'name': i.find('h2').find('a').string,
            'url': base['home_url'] + i.find('a').get('href'),
            'pic': other.pic_show(other.add_https(i.find('img').get('src'))),
            'from': 'fcdm'
        })
    return result


def detail_analysis(html):
    soup = BeautifulSoup(html, 'lxml')
    play = []
    model = []
    there
    return {
        'name': name,
        'from': 'fcdm',
        'auther': '没有数据',
        'pic': other.pic_show(other.add_https(soup.find(class_="thumb l").find('img').get('src'))),
        'time': i_s[0].find('a').string + time[0],
        'model': " ".join(model),
        'info': soup.find(class_="info").string,
        'play': play
    }


def video_analysis(iframe):
    soup = BeautifulSoup(iframe, 'lxml')
    try:
        there
    except AttributeError:
        return None
"""
from urllib.parse import quote
import re


web_name = ['fcdm', 'ttt']
web_origin_name = ['风车动漫', '233动漫']

web_name, web_origin_name = dict(zip(web_origin_name, web_name)), dict(zip(web_name, web_origin_name))


def url_change(url):
    return quote(url)


def add_https(url):
    if re.match(r'^http', url) is not None:
        return url
    else:
        return 'https:' + url


def name_change(name):
    # name = re.sub(r'\s*','',name)
    num = re.findall(r'(第[一二三四五六七八九]季)', name)
    try:
        num = num[0]
    except IndexError:
        return name
    name = re.sub(num, '@', name)
    for i, v in {
     '一': '1',
     '二': '2',
     '三': '3',
     '四': '4',
     '五': '5',
     '六': '6',
     '七': '7',
     '八': '8',
     '九': '9'
    }.items():
        num = re.sub(i, v, num)
    return re.sub('@', num, name)


def video_name_change(name):
    num = re.findall(r'第(\d*|\d*\.\d*)[集话]', name)
    if len(num) == 0:
        return name
    if re.match(r'0\d*|\d{2,}', num[0]) is None:
        return '0' + num[0]
    return num[0]


def web_name_change(name):
    try:
        return web_name[name]
    except KeyError:
        try:
            return web_origin_name[name]
        except KeyError:
            return name


if __name__ == '__main__':
    pass
