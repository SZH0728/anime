# -*- coding:utf-8 -*-

# ======================================================================================================================
# ANIME DOWNLOAD
# AUTHOR: SUN
# DESCRIPTION: 浏览+解析器
# ======================================================================================================================

from network import broswer
from threading import Thread, Lock
from concurrent.futures import ProcessPoolExecutor
from requests import get
from time import sleep

request = 'request'
driver = 'driver'


class view_code(object):
    def __init__(self, url, use, analysis_=None):
        self.url = url
        self.analysis = analysis_
        self.use = use
        self.result = None
        self._html = ''
        self._done = False

    def html(self, html):
        self._html = html
        if self.analysis is not None:
            self.result = self.analysis(html)
        self._done = True

    @property
    def wait_for_html(self):
        if self._html == '':
            return True
        else:
            return False

    @property
    def done(self):
        return self._done


class analysis(Thread):
    def __init__(self, broswer_, driver_, worker=5):
        super(analysis, self).__init__()
        self._broswer = broswer.driver(broswer_, driver_)
        self._pool = ProcessPoolExecutor(worker)
        self._all_task = {}
        self._url_list = {}
        self._lock = Lock()
        self.stop = False
        Thread.start(self)

    @staticmethod
    def html_get(url):
        return get(url=url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }).content

    def run(self):
        while not self.stop:
            sleep(1)
            for key, value in list(self._all_task.items()):
                if self.stop is True:
                    break
                self._lock.acquire()
                self._url_list[key].html(value.result())
                del self._all_task[key]
                self._lock.release()
            if self.stop is True:
                break
            for i in list(self._url_list.values()):
                if self.stop is True:
                    break
                if i.done is True:
                    continue
                if i.use != driver:
                    continue
                a = self._broswer.get(i.url, False, 1)
                if a is not None:
                    self._lock.acquire()
                    self._url_list[i].html(self._broswer.get(i, True))
                    self._lock.release()

    def add_request(self, url, analysis_):
        self._all_task[url] = self._pool.submit(self.html_get, url)
        self._url_list[url] = view_code(url, request, analysis_)

    def add_broswer(self, page, url, analysis_, priority=3):
        self._broswer.new_page(page, url, priority)
        self._url_list[url] = view_code(url, driver, analysis_)

    def get(self, url, dele=True, timeout=10):
        for _ in range(timeout):
            try:
                r = self._url_list[url]
                if dele is True:
                    self._lock.acquire()
                    del self._url_list[url]
                    self._lock.release()
                return r.result
            except KeyError:
                sleep(1)
                continue
        return None

    def wait_for_result(self):
        while True:
            sleep(1)
            for key, value in list(self._url_list.items()):
                sleep(1)
                if value.done is True:
                    r = value.result
                    self._lock.acquire()
                    del self._url_list[key]
                    self._lock.release()
                    if r is not None:
                        return r

    def quit(self):
        self.stop = True
        self._broswer.quit()
        del self._pool


if __name__ == '__main__':
    import broswer
    def an(html):
        return html[0]
    a = analysis(broswer.broswer_option(), broswer.driver_option())
    a.add_request('https://hao.360.com/?src=lm&ls=n4bf4a0c099', an)
    print(a.wait_for_result())
    pass
