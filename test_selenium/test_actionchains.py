# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/7/22
Project ： PyCharm
File  : test_actionchains
E-mail: zh13997821732@163.com


================================================================================

"""
import pytest
import selenium
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains():

    def setup(self):
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
    @pytest.mark.skip
    def test_click(self):
        # 单击、双击、右键
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath('//form[@name = "f1"]/input[3]')
        element_right_click = self.driver.find_element_by_xpath('//form[@name = "f1"]/input[4]')
        element_double_click = self.driver.find_element_by_xpath('//form[@name = "f1"]/input[2]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_right_click)
        action.double_click(element_double_click)
        # 使用 Actionchains 以后需要调用perform来执行所有存储的操作
        action.perform()
        sleep(5)
    @pytest.mark.skip
    def test_moveto_element(self):
        self.driver.get('http://www.baidu.com')
        move_element=self.driver.find_element_by_xpath('//span[@id = "s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(move_element)
        action.perform()
        sleep(5)
    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get('https://sahitest.com/demo/dragDropMooTools.htm')
        drag_element= self.driver.find_element_by_id('dragger')
        drop_element= self.driver.find_element_by_xpath('//body//div[5]')
        action = ActionChains(self.driver)
        # 第一个传入的是drag_element拖动并按住元素 第二个传入的是需要在拖动到相关元素后释放的元素drop_element
        # action.drag_and_drop(drag_element, drop_element).perform()
        #                    选择元素并按住不放       拖到drop元素后释放  展示所有存储的操作
        # action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()#按住不放，并且移动到某个元素上再释放
        sleep(3)
        
    def test_sendkeys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        action = ActionChains(self.driver)   #实例化
        ele.click()
        action.send_keys("username").pause(1)  #输入username
        action.send_keys(Keys.SPACE).pause(1)  # 空格
        action.send_keys("tom").pause(1)      # 输入tom
        action.send_keys(Keys.BACK_SPACE).perform()  #展示所有存储的操作
        sleep(3)


