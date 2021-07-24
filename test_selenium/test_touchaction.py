# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/7/22
Project ： PyCharm
File  : test_111
E-mail: zh13997821732@163.com


================================================================================

"""
import configparser
from time import sleep
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction():

    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("w3c", False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_scrollbottom(self):
        self.driver.get('http://www.baidu.com')
        el = self.driver.find_element_by_id("kw")
        el_search = self.driver.find_element_by_id("su")
        el.send_keys("selenium测试")
        action = TouchActions(self.driver)
        # action.tap为要点击的元素
        action.tap(el_search)
        action.perform()
        # 滑动，从el_search元素开始，X轴偏移0 Y轴偏移10000
        action.scroll_from_element(el_search, 0, 10000).perform()
        sleep(3)