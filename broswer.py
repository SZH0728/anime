# -*- coding:utf-8 -*-

# ======================================================================================================================
# ANIME DOWNLOAD
# AUTHOR: SUN
# DESCRIPTION: webdriver的方法封装
# ======================================================================================================================

from random import choice
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import threading
import time
import queue
from requests import get
import os

js = 'window.open("%s");'
chrome_path = r'D:\project\Chrome-bin\chrome.exe'


def add(url, by=By.XPATH, xpath=None, priority=3, timeout=8, other=None):
    return Task(priority, {
        'url': url,
        'by': by,
        'xpath': xpath,
        'timeout': timeout,
        'other': other if other is not None else []
    })


def driver_setting(proxy="", show=False, pic=False, size=False):
    # 浏览器设置
    options = webdriver.ChromeOptions()

    options.binary_location = chrome_path
    options.add_argument('--disable-gpu')
    options.add_argument('disable-infobars')
    if proxy != "":
        options.add_argument('proxy-server=' + proxy)
    if show is False:
        options.add_argument('--headless')
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
    if pic is False:
        options.add_experimental_option('prefs', {"profile.managed_default_content_settings.images": 2})
    if size is True:
        options.add_argument('--start-maximized')
    return options


def view_setting(max_request=0, max_view=8):
    # 使用设置
    return {
        'max_request': max_request,
        'max_view': max_view
    }


def pic_download(url, path, name):
    # 图片下载
    with open(os.path.join(path, name), 'wb') as p:
        response = get(url=url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        })
        p.write(response.content)
        p.close()


def video_download(url, path, name):
    # 视频下载
    size = 0
    response = get(url=url, stream=True, headers={
                 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
                })
    chunk_size = 1024
    content_size = int(response.headers['content-length'])  # 文件大小
    print(name)
    print("文件大小：" + str(round(float(content_size / chunk_size / 1024), 4)) + "[MB]")
    with open(os.path.join(path, name+'.mp4'), 'wb') as file:
        for data in response.iter_content(chunk_size=chunk_size):
            file.write(data)
            size += len(data)
            print('\r' + "已经下载：" + int(size / content_size * 10) * "█" + " [" + str(
                round(float(size / content_size) * 100, 2)) + "%" + "]" + " [" + str(
                round(size / chunk_size / 1024, 2)) + "MB]", end="")
        file.close()
        print('')
        print('')


class timer(object):
    # 单个计时器
    def __init__(self):
        self.start = time.time()

    def end(self):
        return time.time()-self.start


class timers(object):
    # 多个计时器
    def __init__(self):
        self.start_list = {}

    def start(self, name):
        self.start_list[name] = time.time()

    def end(self, name):
        return time.time()-self.start_list[name]

    def dele(self, name):
        del self.start_list[name]

    @property
    def name(self):
        return self.start_list.keys()


class Task(object):
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name

    def __str__(self):
        return "Task(priority={p}, name={n})".format(p=self.priority, n=self.name)

    def __lt__(self, other):
        return self.priority <= other.priority


class broswer(object):
    # 父类，不可直接使用
    def __init__(self, view_set, driver_set=driver_setting()):
        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities["pageLoadStrategy"] = "none"
        self.driver = webdriver.Chrome(options=driver_set, desired_capabilities=desired_capabilities)

        self.que = queue.PriorityQueue(maxsize=view_set['max_request'])
        self.lock = threading.Lock()
        self.result = {}
        self.start = threading.Event()
        self.start.set()

        self.thread = threading.Thread(target=self.main)
        self.thread.setDaemon(True)
        self.thread.start()

    def main(self):
        # 子类的重写方法
        pass

    def html(self):
        num = len(self.driver.find_elements(By.TAG_NAME, 'iframe'))
        iframe = []
        if num != 0:
            for n in range(0, num):
                self.driver.switch_to.frame(n)
                iframe.append(self.html())
                self.driver.switch_to.parent_frame()
        else:
            iframe = None
        return {
            'html': self.driver.page_source,
            'iframe': iframe
        }

    def adds(self, *args):
        # 加入多个请求 *传入add函数，而非方法
        for i in args:
            self.que.put(i)

    def add(self, url, by=By.XPATH, xpath=None, priority=3, timeout=8, other=None):
        # 加入单个请求
        self.que.put(Task(priority, {
            'url': url,
            'by': by,
            'xpath': xpath,
            'timeout': timeout,
            'other': other if other is not None else []
        }))

    def get(self, url=None, others=None, dele=True, wait=True, timeout=8):
        # 获取结果
        t = timer()
        while True:
            if url is not None:
                try:
                    ru = self.result[url]
                except KeyError:
                    if not wait:
                        break
                else:
                    if dele:
                        self.lock.acquire()
                        del self.result[url]
                        self.lock.release()
                    return ru
            elif others is not None:
                ru = []
                for i in self.result.values():
                    if others in dict(i)['other']:
                        ru.append(i)
                return ru
            else:
                if wait or t.end() > timeout:
                    break
        return None

    def random(self, dele=True):
        # 随机抽取结果
        if len(self.result) == 0:
            return None
        r = choice(list(self.result.keys()))
        v = self.result[r]
        if dele:
            self.lock.acquire()
            del self.result[r]
            self.lock.release()
        return v

    def quit(self):
        # 结束线程
        self.start.clear()
        self.thread.join()
        self.driver.quit()


class broswer_one(broswer):
    # 单界面
    def __init__(self, driver_set, view_set):
        super(broswer_one, self).__init__(view_set, driver_set)

    def main(self):
        while self.start.is_set():
            while True:
                option = {}
                if self.que.empty() is not True:
                    option = self.que.get().name
                    break
                else:
                    if self.start.is_set() is False:
                        break
                time.sleep(2)
            if self.start.is_set() is False:
                break
            t = timer()
            self.driver.get(option['url'])
            while self.start.is_set():
                if option['xpath'] is not None:
                    try:
                        self.driver.find_element(option['by'], option['xpath'])
                    except selenium.common.exceptions.NoSuchElementException:
                        if t.end() > option['timeout']:
                            self.lock.acquire()
                            self.result[option['url']] = {
                                'main': None,
                                'other': option['other']
                            }
                            self.lock.release()
                            break
                    else:
                        self.lock.acquire()
                        self.result[option['url']] = {
                            'main': broswer.html(self),
                            'other': option['other']
                        }
                        self.lock.release()
                        break
                else:
                    if t.end() > option['timeout']:
                        self.lock.acquire()
                        self.result[option['url']] = {
                            'main': broswer.html(self),
                            'other': option['other']
                        }
                        self.lock.release()
                        break


class broswer_more(broswer):
    # 多界面
    def __init__(self, driver_set, view_set):
        self.view_set = view_set
        self._option = {}
        super(broswer_more, self).__init__(view_set, driver_set)

    def main(self):
        t = timers()
        home = self.driver.window_handles[0]
        while self.start.is_set():
            while self.view_set['max_view'] >= len(self._option):
                if self.que.empty() is not True:
                    option = self.que.get().name
                    self._option[option['url']] = option
                    t.start(option['url'])
                    self.driver.switch_to.window(home)
                    self.driver.execute_script(js % option['url'])
                    self._option[option['url']]['header'] = self.driver.window_handles[-1]
                    time.sleep(0.5)
                else:
                    if self.start.is_set() is False:
                        break
                    if len(self._option) != 0:
                        break
                time.sleep(2)
            if self.start.is_set() is False:
                break
            for url, option in list(self._option.items()):
                self.driver.switch_to.window(option['header'])
                if option['xpath'] is not None:
                    try:
                        self.driver.find_element(option['by'], option['xpath'])
                    except selenium.common.exceptions.NoSuchElementException:
                        if t.end(url) > option['timeout']:
                            self.lock.acquire()
                            self.result[option['url']] = {
                                'main': None,
                                'other': option['other']
                            }
                            self.lock.release()
                            del self._option[url]
                            self.driver.close()
                            t.dele(url)
                    else:
                        self.lock.acquire()
                        self.result[option['url']] = {
                            'main': broswer.html(self),
                            'other': option['other']
                        }
                        self.lock.release()
                        del self._option[url]
                        self.driver.close()
                        t.dele(url)
                else:
                    if t.end(url) > option['timeout']:
                        self.lock.acquire()
                        self.result[option['url']] = {
                            'main': broswer.html(self),
                            'other': option['other']
                        }
                        self.lock.release()
                        del self._option[url]
                        self.driver.close()
                        t.dele(url)
            if self.start.is_set() is False:
                break
            time.sleep(0.5)


class download(object):
    def __init__(self, driver_set, path):
        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities["pageLoadStrategy"] = "none"
        self.driver = webdriver.Chrome(options=driver_set, desired_capabilities=desired_capabilities)

        self.path = path
        self.start = threading.Event()
        self.start.set()

        self._t1 = threading.Thread(target=self._broswer)
        self._t2 = threading.Thread(target=self._download)

        self._t1.setDaemon(True)
        self._t2.setDaemon(True)

        self.request = queue.Queue()
        self._response = queue.Queue(maxsize=1)

        self._t1.start()
        self._t2.start()

        self.error = ''

    def _broswer(self):
        while self.start.is_set():
            while True:
                option = {}
                if self.request.empty() is not True:
                    option = self.request.get()
                    break
                else:
                    if self.start.is_set() is False:
                        break
                time.sleep(2)
            if self.start.is_set() is False:
                break
            for i in option['play']:
                try:
                    a = os.path.exists(os.path.join(os.path.join(os.path.join(self.path, option['name']),
                                                                 os.path.join(option['from'], option['list'])),
                                                    i['name']))
                except KeyError:
                    a = os.path.exists(os.path.join(os.path.join(self.path, option['name']),
                                                    os.path.join(option['from'], i['name'])))
                except TypeError:
                    a = os.path.exists(os.path.join(os.path.join(self.path, option['name']),
                                                    os.path.join(option['from'], i['name'])))
                if a:
                    print('文件已存在，将自动跳过')
                    continue
                self.driver.get(i['url'])
                time.sleep(10)
                result = self.analysis(self._html(), option['from'])
                if result is None:
                    print('该列表无法下载')
                    break
                else:
                    self._response.put({
                        'all': option['name'],
                        'name': i['name'],
                        'url': result,
                        'from': option['from'],
                        'list': option['list']
                    }, True, 100000)

    def _html(self):
        num = len(self.driver.find_elements(By.TAG_NAME, 'iframe'))
        iframe = []
        if num != 0:
            for n in range(0, num):
                self.driver.switch_to.frame(n)
                iframe.append(self._html())
                self.driver.switch_to.parent_frame()
        else:
            iframe = None
        return {
            'html': self.driver.page_source,
            'iframe': iframe
        }

    def analysis(self, html, come):
        return html, come

    def _download(self):
        while self.start.is_set():
            while True:
                url = {}
                if self._response.empty() is not True:
                    url = self._response.get()
                    break
                else:
                    if self.start.is_set() is False:
                        break
                time.sleep(2)
            if self.start.is_set() is False:
                break
            else:
                path = os.path.join(self.path, url['all'])
                if not os.path.exists(path):
                    os.mkdir(path)
                path = os.path.join(path, url['from'])
                if not os.path.exists(path):
                    os.mkdir(path)
                if url['list'] is not None:
                    path = os.path.join(path, url['list'])
                    if not os.path.exists(path):
                        os.mkdir(path)
                for i in range(3):
                    try:
                        video_download(url['url'], path, url['name'])
                        break
                    except BaseException as e:
                        print('无法下载，因为：'+str(e))
                    finally:
                        if i == 3:
                            self.error = url['name']

    def add(self, name, come, play, lis=None):
        self.request.put({
            'name': name,
            'from': come,
            'list': lis,
            'play': play
        })

    def quit(self):
        self.start.clear()
        self._t1.join()
        self._t2.join()
        self.driver.quit()


if __name__ == '__main__':
    a = broswer_one(driver_setting(show=True), view_setting())
    a.add(url='https://www.dm233.cc/search?keyword=%E9%BB%84%E9%87%91&seaex=1')
    time.sleep(10000)
    pass
