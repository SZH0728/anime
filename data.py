# -*- coding:utf-8 -*-

# ======================================================================================================================
# ANIME DOWNLOAD
# AUTHOR: SUN
# DESCRIPTION: 数据存储
# ======================================================================================================================

from network import picture
from concurrent.futures import ProcessPoolExecutor, as_completed
from threading import Thread, Event
from time import sleep
from re import findall


class research_result(object):
    def __init__(self, name, url, pic_url, from_):
        self.name = name
        self.url = url
        self.pic_url = pic_url
        self._pic = ''
        self.from_ = from_
        try:
            self.fmat = findall(r'(\..{3}?)$', pic_url)[0]
        except IndexError:
            self.fmat = '.jpg'

    @property
    def pic(self):
        if self._pic != '':
            return self._pic
        else:
            self._pic = picture.pic_get(self.pic_url)
            return self._pic

    @property
    def has_pic(self):
        if self._pic == '':
            return False
        else:
            return True

    def set_pic(self, pic):
        self._pic = pic


class research(Thread):
    def __init__(self, worker=5):
        super(research, self).__init__()
        self.result = []
        self.key_word = ''
        self._pool = ProcessPoolExecutor(worker)
        self._pool_task = {}
        self._flag = Event()
        self._stop_ = False
        Thread.start(self)

    def run(self):
        while not self._stop_:
            for value in as_completed(self._pool_task.values()):
                try:
                    key = list(self._pool_task.keys())[list(self._pool_task.values()).index(value)]
                    result = self.search_by_pic_url(key)
                except (KeyError, IndexError):
                    continue
                result.set_pic(value.result())
                del self._pool_task[key]
                if len(self._pool_task) == 0:
                    self._flag.clear()
                if self._stop_:
                    break
            if self._stop_:
                break
            self._flag.wait(3)

    def add_result(self, name, url, pic_url, from_):
        self.result.append(research_result(name, url, pic_url, from_))
        self._pool_task[pic_url] = self._pool.submit(picture.pic_get, pic_url)
        self._flag.set()

    def search_by_name(self, name):
        for i in self.result:
            if i.name == name:
                return i
        return None

    def search_by_url(self, url):
        for i in self.result:
            if i.url == url:
                return i
        return None

    def search_by_pic_url(self, pic_url):
        for i in self.result:
            if i.pic_url == pic_url:
                return i
        return None

    def search_all_by_name(self, name):
        r = []
        for i in self.result:
            if i.name == name:
                r.append(i)
        return r if r != [] else None

    def search_all_by_from(self, from_):
        r = []
        for i in self.result:
            if i.from_ == from_:
                r.append(i)
        return r if r != [] else None

    def clear(self):
        for i in self._pool_task.values():
            i.cancel()
        self._pool_task.clear()
        self.result.clear()

    def wait_for_complete(self):
        while True:
            if len(self._pool_task) == 0:
                break
            sleep(1)

    def stop(self):
        self._stop_ = True
        del self._pool

    @property
    def is_load_complete(self):
        if len(self._pool_task) == 0:
            return True
        else:
            return False


class download_list(object):
    def __init__(self, list_name, url_list):
        self.list_name = list_name
        self.url_list = url_list

    def research_by_name(self, name):
        r = []
        for key, value in enumerate(self.url_list):
            if key == name:
                r.append({
                    'name': key,
                    'url': value
                })
        return r

    def research_by_url(self, url):
        for key, value in enumerate(self.url_list):
            if value == url:
                return {
                    'name': key,
                    'url': value
                }
        return None


class detail(object):
    def __init__(self):
        self.name = ''
        self.url = ''
        self.picture = ''
        self.picture_url = ''
        self._download_list = {}
        self.introduce = ''
        self.from_ = ''
        self.fmat = ''
        self.auther = ''
        self.time = ''
        self.type = ''

    def put_research_result(self, result):
        self.name = result.name
        self.url = result.url
        self.picture = result.pic
        self.picture_url = result.pic_url
        self.from_ = result.from_
        self.fmat = result.fmat

    def set_download_list(self, auther, time, type_, introduce, lis):
        self.auther = auther
        self.time = time
        self.type = type_
        self.introduce = introduce
        for i in lis:
            self._download_list[i.list_name] = i

    @property
    def clear_download_list(self):
        r = {}
        for key, value in self._download_list.items():
            if len(value.url_list) == 0:
                continue
            r[key] = value.url_list
        return r

    @property
    def download_list(self):
        return self._download_list


if __name__ == '__main__':
    # a = research()
    # a.add_result('黄金拼图 Thank you!!', '/view/22329.html',
    #              'https://tva4.sinaimg.cn/large/008kBpBlgy1grvxh6cyvtj305i07n3zd.jpg')
    # a.add_result("黄金拼图剧场版 Pretty Days", "/view/17264.html",
    #              'https://sc04.alicdn.com/kf/Ha856ab0982b94c88b4ca0716c6d440acF.jpg')
    # a.wait_for_complete()
    # print(a.result)
    pass
