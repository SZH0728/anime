# -*- coding:utf-8 -*-

# ======================================================================================================================
# ANIME DOWNLOAD
# AUTHOR: SUN
# DESCRIPTION: 视频下载
# ======================================================================================================================

from network import broswer
from PyQt5 import QtWidgets, QtCore
from selenium.webdriver import Chrome
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread, Lock
from sqlite3 import connect


class condition(object):
    wait_for_analysis = 'wait_for_analysis'
    wait_for_download = 'wait_for_download'
    downloading = 'downloading'
    download_error = 'download_error'
    complete = 'complete'


class download_event(object):
    signal = QtCore.pyqtSignal(float)

    def __init__(self, url, name):
        self.codition = condition.wait_for_analysis
        self.url = url
        self.name = name
        self.video_url = ''
        self.m3u8 = None

    def set_analysis_result(self, video_url, m3u8=False):
        self.video_url = video_url
        self.m3u8 = m3u8
        self.codition = condition.wait_for_download


class download_group(object):
    def __init__(self, method, *args: download_event):
        self.method = method
        self.list = []
        for i in args:
            self.list.append(i)

    def append(self, *args: download_event):
        for i in args:
            self.list.append(i)

    def find_by_name(self, name):
        for i in self.list:
            if i.name == name:
                return i
        return None

    def find_by_url(self, url):
        for i in self.list:
            if i.url == url:
                return i
        return None

    def find_by_video_url(self, video_url):
        for i in self.list:
            if i.video_url == video_url:
                return i
        return None

    def analysis_all_events(self):
        for i in self.list:
            if i.video_url is not None:
                yield i.url


class group_list(object):
    def __init__(self):
        self.dict = []

        # 通过__getitem__使用mytree[3]获取值的方式，否则不能使用mytree[3]方法获取值
    def __getitem__(self, key):
        return self.dict[key]

        # 通过__setitem__使用mytree[3]="red"方式，否则不能使用mytree[3]="red"方法
    def __setitem__(self, key, value):
        self.dict[key] = value

        # 通过__delitem__调用del方法，否则不能使用del方法
    def __delitem__(self, key):
        del self.dict[key]

        # 通过__len__调用len()方法，否则不能使用len()方法
    def __len__(self):
        return len(self.dict)

        # 通过__contains__调用in方法，若一个集合类型没有实现__contains__方法，那么in运算符就会按顺序做一次迭代搜索。
    def __contains__(self, key):
        return key in self.dict


# class table(Thread):
#     def __init__(self, table_: QtWidgets.QTableWidget, path: str):
#         super(table, self).__init__()
#         self.table = table_
#         self.path = path
#         self.keep = True
#         self.driver_option = broswer.driver_option()
#         self.driver_option.max_load = 1
#         self.all_list = []
#         self.lock = Lock()
#         self.start()
#
#     def run(self):
#         desired_capabilities = DesiredCapabilities.CHROME
#         desired_capabilities["pageLoadStrategy"] = "none"
#         self.broswer = Chrome(options=broswer.broswer_option(True).options,
#                               desired_capabilities=desired_capabilities,
#                               executable_path=r'D:\project\Anime\chromedriver.exe')
#         self.driver = broswer.control(self.driver_option, self.broswer)
#         while self.keep:
#             for i in self.all_list:
#                 while self.keep:
#                     url = i.get_load()
#                     if url is not None:
#                         self.driver.put_page()
#                         result = self.driver.wait_for_result(60, True)
#                     else:
#                         break
#
#     def add_list(self, li: download_group):
#         self.lock.acquire()
#         self.all_list.append(li)
#         self.lock.release()
class data(object):
    def __init__(self):
        self.connect = connect('./history.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXIST event(url TEXT PRIMARY KEY, name TEXT, from TEXT)')
        self.group = []
        for i in self.cursor.execute('SELECT * FROM event'):
            self.group.append(download_group())


if __name__ == '__main__':
    pass
