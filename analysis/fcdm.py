# -*- coding:utf-8 -*-

# ======================================================================================================================
# ANIME DOWNLOAD
# AUTHOR: SUN
# DESCRIPTION: 风车动漫网页解析
# ======================================================================================================================

from bs4 import BeautifulSoup
from analysis import other
from broswer import add
import re

base = {
    'home_url': 'https://www.dm530p.org',
    'research_url': 'https://www.dm530p.net/s_all?ex=1&kw=%s'
}


def research(name):
    return add(
        url=base['research_url'] % other.url_change(name),
        xpath='/html/body/div[4]/div[2]',
        other=['fcdm', 'research']
    )


def detail(url):
    return add(
        url=url,
        xpath='/html/body/div[2]/div[2]',
        other=['fcdm', 'detail'],
        timeout=15
    )


def home_analysis(html):
    soup = BeautifulSoup(html, 'lxml')
    every = [[], [], [], [], [], [], []]
    week = []
    main = {}
    head = []
    for index, i in enumerate(soup.find(class_="tlist").find_all("ul")):
        for p in i.find_all('li'):
            every[index].append({
             'name': p.find_all('a')[1].string,
             'url': base['home_url'] + p.find_all('a')[1].get('href')
             })
    for i in soup.find(class_='side r').find_all(class_='bg', limit=2)[1].find(class_='pics').find_all('li'):
        week.append({
         'name': i.find('h2').find('a').string,
         'url': base['home_url'] + i.find('a').get('href'),
         'pic': base['home_url'] + i.find('img').get('src')
         })
    for n, v in zip(soup.find(class_='firs l').find_all(class_='dtit'),
                    soup.find(class_='firs l').find_all(class_='img')):
        main[n.find('a').string] = []
        for i in v.find_all('li'):
            main[n.find('a').string].append({
             'name': i.find('p').find('a').string,
             'url': base['home_url'] + i.find('a').get('href'),
             'pic': base['home_url'] + i.find('img').get('src')
             })
    for i in soup.find_all(class_='heros'):
        for p in i.find_all('li'):
            head.append({
                'name': p.find('a').get('title'),
                'url': base['home_url'] + p.find('a').get('href'),
                'pic': base['home_url'] + p.find('img').get('src')
            })
    return [every, week, main, head]


def research_analysis(html):
    soup = BeautifulSoup(html, 'lxml')
    result = []
    for i in soup.find(class_='lpic').find_all('li'):
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
    name = other.name_change(soup.find(class_="thumb l").find('a').string)
    sinfo = soup.find(class_="sinfo")
    i_s = sinfo.find_all('span')
    time = re.findall(r'</a>(.*?)\s*?</span>', str(i_s[0]))
    for index, i in enumerate(soup.find(id='main0').find_all(class_="movurl")):
        play.append([])
        for p in i.find_all('li'):
            play[index].append({
                'name': other.video_name_change(p.find('a').string),
                'url': base['home_url'] + p.find('a').get('href')
            })
    for i in i_s[2].find_all('a'):
        model.append(i.string)
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
        return soup.find('video').get('src')
    except AttributeError:
        return None


if __name__ == '__main__':
    pass
