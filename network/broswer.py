# -*- coding:utf-8 -*-

# ======================================================================================================================
# ANIME DOWNLOAD
# AUTHOR: SUN
# DESCRIPTION: 
# ======================================================================================================================

import selenium.common.exceptions
from selenium.webdriver import Chrome, ChromeOptions
from threading import Thread, Event, Lock
from time import sleep, time
from queue import PriorityQueue

js = 'window.open("%s");'
chrome_path = r'D:\project\Chrome-bin\chrome.exe'


class By(object):
    """
    Set of supported locator strategies.
    """

    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"


class Task(object):
    def __init__(self, priority: int, name):
        self.priority = priority
        self.name = name

    def __str__(self):
        return "Task(priority={p}, name={n})".format(p=self.priority, n=self.name)

    def __lt__(self, other):
        return self.priority <= other.priority


class timer(object):
    # 单个计时器
    def __init__(self):
        self.start = time()

    def end(self):
        return time()-self.start

    def clear(self):
        self.start = time()

    def timeout(self, time_out: float):
        if self.end() < time_out:
            return False
        else:
            return True


class driver_control(object):
    def __init__(self, driver: Chrome):
        self.driver = driver

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_element_by_id(self, id_):
        return self.driver.find_element(By.ID, id_)

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def find_element_by_name(self, name):
        return self.driver.find_element(By.NAME, name)

    def find_element_by_class_name(self, class_name):
        return self.driver.find_element(By.CLASS_NAME, class_name)

    def find_element_by_tag_name(self, tag_name):
        return self.driver.find_element(By.TAG_NAME, tag_name)

    def find_element_by_css_selector(self, css_selector):
        return self.driver.find_element(By.CSS_SELECTOR, css_selector)

    def find_element_by_link_text(self, link_text):
        return self.driver.find_element(By.LINK_TEXT, link_text)

    def find_element_by_partial_link_text(self, partial_link_text):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, partial_link_text)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def find_elements_by_id(self, id_):
        return self.driver.find_elements(By.ID, id_)

    def find_elements_by_xpath(self, xpath):
        return self.driver.find_elements(By.XPATH, xpath)

    def find_elements_by_name(self, name):
        return self.driver.find_elements(By.NAME, name)

    def find_elements_by_class_name(self, class_name):
        return self.driver.find_elements(By.CLASS_NAME, class_name)

    def find_elements_by_tag_name(self, tag_name):
        return self.driver.find_elements(By.TAG_NAME, tag_name)

    def find_elements_by_css_selector(self, css_selector):
        return self.driver.find_elements(By.CSS_SELECTOR, css_selector)

    def find_elements_by_link_text(self, link_text):
        return self.driver.find_elements(By.LINK_TEXT, link_text)

    def find_elements_by_partial_link_text(self, partial_link_text):
        return self.driver.find_elements(By.PARTIAL_LINK_TEXT, partial_link_text)

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def execute_script(self, js_):
        self.driver.execute_script(js_)

    @property
    def page_source(self):
        return self.driver.page_source


class broswer_option(object):
    def __init__(self, all_false=False):
        self.options = ChromeOptions()

        self.options.binary_location = chrome_path
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('disable-infobars')

        if all_false is True:
            self.set_show_false()
            self.set_show_picture_false()

    def set_proxy(self, proxy: str):
        self.options.add_argument('proxy-server=' + proxy)

    def set_show_false(self):
        self.options.add_argument('--headless')
        self.options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36')
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])

    def set_show_picture_false(self):
        self.options.add_experimental_option('prefs', {"profile.managed_default_content_settings.images": 2})

    def set_size_true(self):
        self.options.add_argument('--start-maximized')


class driver_option(object):
    def __init__(self):
        self.max_wait = 0
        self.max_load = 5


class page(Thread, driver_control):
    def __init__(self, control_, driver: Chrome, url: str, header=''):
        Thread.__init__(self)
        driver_control.__init__(self, driver)
        self._header = header
        self.url = url
        self.control = control_
        self.start()
        self.value = None

    def operate(self):
        pass

    def run(self):
        if self._header == '':
            self.control.get_control(self)
            self.execute_script(js % self.url)
            self._header = self.driver.window_handles[-1]
            self.driver.switch_to.window(self._header)
            self.operate()
        else:
            self.control.get_control(self)
            self.driver.switch_to.window(self._header)
            self.operate()
        self.driver.close()
        self.control.return_control(self, True)

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        if self.header == '':
            self._header = value
        else:
            raise ValueError('已存在header:'+self._header)

    @property
    def html(self):
        num = len(self.driver.find_elements(By.TAG_NAME, 'iframe'))
        iframe = []
        if num != 0:
            for n in range(0, num):
                self.driver.switch_to.frame(n)
                iframe.append(self.html)
                self.driver.switch_to.parent_frame()
        else:
            iframe = None
        return {
            'html': self.driver.page_source,
            'iframe': iframe
        }

    def element_is_exist(self, by, value):
        try:
            self.driver.find_element(by, value)
            return True
        except selenium.common.exceptions.NoSuchElementException:
            return False

    def wait_for_second(self, time_):
        t = timer()
        while not t.timeout(time_):
            self.control.return_control(self, False)
            self.control.get_control(self)
            self.driver.switch_to.window(self.header)

    def wait_for_element(self, by, value):
        while not self.element_is_exist(by, value):
            self.control.return_control(self, False)
            self.control.get_control(self)
            self.driver.switch_to.window(self.header)

    def new_page_appear(self, page_, url):
        page_ = page_(self.control, url, self.driver.window_handles[0])
        self.control.put_page(page_)


class control(Thread):
    def __init__(self, option: driver_option, driver: Chrome):
        super(control, self).__init__()
        self.option = option
        self.driver = driver
        self._que = PriorityQueue()
        self._load_pages = {}
        self._wait_pages = {}
        self._home_page = self.driver.window_handles[0]
        self.result = {}
        self._lock = Lock()
        self._control_page = None
        self.keep = True
        self.start()

    def run(self):
        last = 0
        while self.keep:
            if len(self._load_pages) <= self.option.max_load and len(self._wait_pages) != 0:
                one = self._que.get()
                try:
                    self._load_pages[one.name.url] = self._wait_pages[one.name.url]
                    del self._wait_pages[one.name.url]
                except KeyError:
                    self._que.put(one)
            if self._control_page is None:
                try:
                    list(self._load_pages.values())[last].set()
                except IndexError:
                    pass
                if last < len(self._load_pages)-1:
                    last += 1
                else:
                    last = 0
            sleep(1)

    def get_control(self, page_: page):
        if page_.url in self._load_pages.keys():
            self._load_pages[page_.url].wait()
        elif page_.url in self._wait_pages.keys():
            self._wait_pages[page_.url].wait()
        else:
            self._lock.acquire()
            self._wait_pages[page_.url] = Event()
            self._lock.release()
            self._wait_pages[page_.url].clear()
            try:
                self._wait_pages[page_.url].wait()
            except KeyError:
                self._load_pages[page_.url].wait()
        self._control_page = page_

    def return_control(self, page_: page, done: bool):
        if done:
            self._control_page = None
            del self._load_pages[page_.url]
            self._lock.acquire()
            self.result[page_.url] = page_.value
            self._lock.release()
        else:
            self._control_page = None
            self._load_pages[page_.url].clear()

    def get_result(self, url: str, dele=True):
        if url not in self.result.keys():
            return None
        r = self.result[url]
        if dele:
            self._lock.acquire()
            del self.result[url]
            self._lock.release()
        return r

    def wait_for_result(self, timeout: int, dele: bool):
        t = timer()
        r = None
        while not t.timeout(timeout):
            if len(self.result) != 0:
                r = list(self.result.values())[0]
                key = list(self.result.keys())[0]
                if dele:
                    self._lock.acquire()
                    del self.result[key]
                    self._lock.release()
                return {key: r}
            sleep(1)
        return r

    def put_page(self, page_: page, priority=5):
        self._que.put(Task(priority, page_))

    def quit(self):
        self.keep = False
        self.driver.quit()


if __name__ == '__main__':
    # from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    # desired_capabilities = DesiredCapabilities.CHROME
    # desired_capabilities["pageLoadStrategy"] = "none"
    # driver_ = Chrome(options=broswer_option().options,
    #                  desired_capabilities=desired_capabilities,
    #                  executable_path=r'D:\project\Anime\chromedriver.exe')
    # c = control(driver_option(), driver_)
    # class example(page):
    #     def operate(self, driver: Chrome):
    #         self.wait_for_second(5)
    #         self.value = self.html
    # c.put_page(example(c, driver_,
    #                    'https://www.dm233.cc/search?keyword=%E9%BB%84%E9%87%91%E6%8B%BC%E5%9B%BE&seaex=1'))
    # c.put_page(example(c, driver_,
    #                    'https://www.baidu.com/'))
    # print('main')
    # print(c.wait_for_result())
    # print(c.wait_for_result())
    # c.quit()
    pass
