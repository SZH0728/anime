# -*- coding:utf-8 -*-

# ======================================================================================================================
# ANIME DOWNLOAD
# AUTHOR: SUN
# DESCRIPTION: 233动漫网页解析
# ======================================================================================================================

from bs4 import BeautifulSoup
from analysis import public
import re
from network.broswer import page, By

base = {
    'home_url': 'https://www.dm233.cc',
    'research_url': 'https://www.dm233.cc/search?keyword=%s&seaex=1'
}


def research(name):
    return base['research_url'] % public.url_change(name)


def research_analysis(html):
    soup = BeautifulSoup(html, 'lxml')
    result = []
    for i in soup.find(class_='dhnew adj1').find_all('li'):
        result.append({
            'name': i.find('a').get('title'),
            'url': base['home_url'] + i.find('a').get('href'),
            'pic_url': public.add_https(i.find('img').get('src')),
            'from': 'ttt'
        })
    return result


def detail_analysis(html):
    soup = BeautifulSoup(html, 'lxml')
    play = []
    info = soup.find(class_='info')
    sinfo = soup.find(class_='normal-nei1 dhxx anime_info').find_all('p')
    for index, i in enumerate(soup.find(class_='normal-nei3').find_all(class_='eplist-eppic')):
        play.append([])
        for p in i.find_all('li'):
            play[index].append({
                'name': public.video_name_change(p.find('p').string),
                'url': base['home_url'] + p.find('a').get('href')
            })
    for index, i in enumerate(soup.find(class_='normal-nei3').find_all(class_='eplist-normal')):
        play.append([])
        for p in i.find_all('li'):
            play[index].append({
                'name': public.video_name_change(p.find('span').string),
                'url': base['home_url'] + p.find('a').get('href')
            })
    b = str(info.find(id='box', class_='info2').find('p'))
    b = re.sub(r'<p>|<strong>简介：</strong>|</p>', '', b)
    b = b.strip()
    return {
        'name': public.name_change(info.find(class_='h1-title').string),
        'from': 'ttt',
        'auther': sinfo[6].string.split('：')[1],
        'time': re.findall(r'(\d*-\d*-\d*)', sinfo[-3].string)[0],
        'type': sinfo[9].string.split('：')[1],
        'info': b,
        'play': play
    }


def video_analysis(iframe):
    soup = BeautifulSoup(iframe, 'lxml')
    try:
        soup.find('video').get('src')
    except AttributeError:
        return None


if __name__ == '__main__':
    pass
