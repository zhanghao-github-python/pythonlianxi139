# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/7/24
Project ： PyCharm
File  : test_from
E-mail: zh13997821732@163.com


================================================================================

"""
from time import sleep

import pytest
import selenium
from selenium import webdriver


class Test_form():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        # self.driver.find_element_by_xpath('//form//input[@class="form-control form-control-lg"]').send_keys('username')
        self.driver.find_element_by_id("user_login").send_keys("122313123")
        self.driver.find_element_by_id("user_password").send_keys('password')
        self.driver.find_element_by_class_name("custom-control-label").click()
        self.driver.find_element_by_xpath('//form//input[@name="commit"]').click()
        sleep(5)


