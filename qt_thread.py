# -*- coding:utf-8 -*-

# ======================================================================================================================
# ANIME DOWNLOAD
# AUTHOR: SUN
# DESCRIPTION: 与PyQt有关的多线程
# ======================================================================================================================

from PyQt5.QtCore import pyqtSignal, QThread
from network import *
from concurrent.futures import ProcessPoolExecutor, as_completed
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Chrome
from requests import get
from time import sleep
from analysis import *


class code(object):
    def __init__(self, url, method):
        self.url = url
        self.method = method

    def result(self, result):
        return self.method(result)


class analysis(QThread):
    research = pyqtSignal(list)
    detail = pyqtSignal(dict)

    def __init__(self, broswer_: broswer.broswer_option, driver_: broswer.driver_option, worker=5):
        super(analysis, self).__init__()
        self.keep = True
        self._pool = ProcessPoolExecutor(worker)
        self.driver_option = driver_
        self.broswer_option = broswer_
        self._all_task = {}
        self._request_task = {}

    def run(self):
        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities["pageLoadStrategy"] = "none"
        self.broswer = Chrome(options=self.broswer_option.options,
                              desired_capabilities=desired_capabilities,
                              executable_path=r'D:\project\Anime\chromedriver.exe')
        self.driver = broswer.control(self.driver_option, self.broswer)
        while self.keep:
            for i in as_completed(list(self._request_task.values())):
                url = list(self._request_task.keys())[list(self._request_task.values()).index(i)]
                result = self._all_task[url].result(i.result())
                if type(result) == list:
                    self.research.emit(result)
                elif type(result) == dict:
                    self.detail.emit(result)
                del self._all_task[url]
                del self._request_task[url]
            url = self.driver.wait_for_result(2, True)
            if url is not None:
                result = self._all_task[list(url.keys())[0]].result(list(url.values()[0]))
                if type(result) == list:
                    self.research.emit(result)
                elif type(result) == dict:
                    self.detail.emit(result)
            sleep(1)

    @staticmethod
    def get_code(url):
        return get(url=url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }).content

    def put_request(self, url, method):
        self._request_task[url] = self._pool.submit(self.get_code, url)
        self._all_task[url] = code(url, method)

    def put_broswer(self, page: broswer.page, method, priority=5):
        for _ in range(10):
            try:
                self.driver.put_page(page, priority)
                self._all_task[page.url] = code(page.url, method)
                break
            except AttributeError:
                pass

    def add_research(self, key, range_):
        if 'fcdm' in range_:
            self.put_request(fcdm.research(key), fcdm.research_analysis)
        if 'ttt' in range_:
            self.put_request(ttt.research(key), ttt.research_analysis)

    def add_detail(self, url, from_):
        if from_ == 'fcdm':
            self.put_request(url, fcdm.detail_analysis)
        elif from_ == 'ttt':
            self.put_request(url, ttt.detail_analysis)


if __name__ == '__main__':
    pass
