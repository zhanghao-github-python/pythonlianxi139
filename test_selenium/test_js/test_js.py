# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/7/30
Project ： PyCharm
File  : test_js
E-mail: zh13997821732@163.com


================================================================================

"""
from time import sleep

from test_selenium.base import Base


class Test(Base):
    def test_js_scroll(self):
        self.driver.get('http://www.baidu.com')
        # 搜索selenium测试
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        # 执行js点击百度一下
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        sleep(3)
        # 滑动到最低端
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        # 点击下一页
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(5)
        # 获取当前页面的页签名字和性能数据
        for code in [
            'return document.title', 'return JSON.stringify(performance.timing) '

        ]:
            print(self.driver.execute_script(code))#打印页签名字和性能数据
