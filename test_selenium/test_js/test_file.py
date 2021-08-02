# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/7/30
Project ： PyCharm
File  : test_file
E-mail: zh13997821732@163.com


================================================================================

"""
from time import sleep

from test_selenium.base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get('https://image.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        # 给定图片路径
        self.driver.find_element_by_id("stfile").send_keys(r"C:\Users\Administrator\Desktop\pythonlianxi139\tupian\u=2116882029,1761299726&fm=26&fmt=auto&gp=0.webp")
        sleep(5)