# -*- coding:utf-8 -*-

# ======================================================================================================================
# ANIME DOWNLOAD
# AUTHOR: SUN
# DESCRIPTION: 
# ======================================================================================================================

from configobj import ConfigObj
import os

__version__ = '1.1.0'

chrome_path = r'D:\project\Chrome-bin\chrome.exe'


class setting(object):
    def __init__(self):
        self.path = os.path.join(os.getcwd(), 'set.ini')
        self.set = ConfigObj(self.path, encoding='UTF8')
        if not os.path.exists(self.path):
            self.create()

    def create(self):
        self.set['save_path'] = os.getcwd()
        self.set['user'] = 'user'
        self.set.write()

    def save(self):
        self.set.write()

    @property
    def save_path(self):
        return self.set['save_path']

    @save_path.setter
    def save_path(self, value):
        self.set['save_path'] = value

    @property
    def user(self):
        return self.user

    @user.setter
    def user(self, value):
        self.set['user'] = value


if __name__ == '__main__':
    setting().create()
