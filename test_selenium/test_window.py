# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/7/25
Project ： PyCharm
File  : test_window
E-mail: zh13997821732@163.com


================================================================================

"""
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from test_selenium.base import Base


class Test_Windows(Base):
    def test_window(self):
        action = ActionChains(self.driver)
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('s-top-loginbtn').click()
        self.driver.find_element_by_xpath('//a[text()="立即注册"]').click()
        sleep(3)
        handle = self.driver.window_handles  # 获取所有窗口句柄
        self.driver.switch_to.window(handle[-1])  # 切换到最后一个窗口句柄
        sleep(1)
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('3213dddx')
        sleep(1)
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('13997821747')
        sleep(1)
        self.driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys('123wwww456')
        sleep(1)
        ele = self.driver.find_element_by_id('TANGRAM__PSP_4__verifyCode')
        action.send_keys_to_element(ele, '1234').send_keys(Keys.SPACE).send_keys(Keys.SPACE).perform()
        sleep(2)
        self.driver.find_element_by_id('TANGRAM__PSP_4__isAgree').click()
        sleep(1)
        self.driver.find_element_by_id('TANGRAM__PSP_4__submit').click()
        sleep(1)
        self.driver.switch_to.window(handle[0]) #切换回第一个窗口
        sleep(1)
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        sleep(1)
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('13997821732')
        sleep(1)
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('Zh123456')
        sleep(1)
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()
        sleep(4)
