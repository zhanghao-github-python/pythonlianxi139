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

import pytest

from test_selenium.base import Base


class TestFile(Base):
    @pytest.mark.skip
    def test_file_upload(self):
        self.driver.get('https://image.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        # 给定图片路径
        self.driver.find_element_by_id("stfile").send_keys(
            r"C:\Users\Administrator\Desktop\pythonlianxi139\tupian\u=2116882029,1761299726&fm=26&fmt=auto&gp=0.webp")
        sleep(5)

    def test_readonly(self):
        self.driver.get('https://www.12306.cn/index/')
        time_element = self.driver.execute_script(
            " a=  document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2021-12-30'")
        sleep(10)
