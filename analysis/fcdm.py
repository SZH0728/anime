# -*- coding:utf-8 -*-

# ======================================================================================================================
# ANIME DOWNLOAD
# AUTHOR: SUN
# DESCRIPTION: 风车动漫网页解析
# ======================================================================================================================

from bs4 import BeautifulSoup
from analysis import public
import re


base = {
    'home_url': 'https://www.dm530p.org',
    'research_url': 'https://www.dm530p.net/s_all?ex=1&kw=%s'
}


def research(name):
    return base['research_url'] % public.url_change(name)


def research_analysis(html):
    soup = BeautifulSoup(html, 'lxml')
    result = []
    for i in soup.find(class_='lpic').find_all('li'):
        result.append({
            'name': i.find('h2').find('a').string,
            'url': base['home_url'] + i.find('a').get('href'),
            'pic_url': public.add_https(i.find('img').get('src')),
            'from': 'fcdm'
        })
    return result


def detail_analysis(html):
    soup = BeautifulSoup(html, 'lxml')
    play = []
    model = []
    name = public.name_change(soup.find(class_="thumb l").find('a').string)
    sinfo = soup.find(class_="sinfo")
    i_s = sinfo.find_all('span')
    time = re.findall(r'</a>(.*?)\s*?</span>', str(i_s[0]))
    for index, i in enumerate(soup.find(id='main0').find_all(class_="movurl")):
        play.append([])
        for p in i.find_all('li'):
            play[index].append({
                'name': public.video_name_change(p.find('a').string),
                'url': base['home_url'] + p.find('a').get('href')
            })
    for i in i_s[2].find_all('a'):
        model.append(i.string)
    return {
        'name': name,
        'from': 'fcdm',
        'auther': '没有数据',
        'time': i_s[0].find('a').string + time[0],
        'type': " ".join(model),
        'info': soup.find(class_="info").string,
        'play': play
    }


def video_analysis(html):
    iframe = html['iframe'][0]
    soup = BeautifulSoup(iframe, 'lxml')
    try:
        return soup.find('video').get('src')
    except AttributeError:
        return None


if __name__ == '__main__':
    pass
