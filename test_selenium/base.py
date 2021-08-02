# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/7/25
Project ： PyCharm
File  : base
E-mail: zh13997821732@163.com


================================================================================

"""
import selenium
from selenium import webdriver


class Base():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()
