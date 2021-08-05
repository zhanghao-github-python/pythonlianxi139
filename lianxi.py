# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/8/4
Project ： PyCharm
File  : lianxi
E-mail: zh13997821732@163.com


================================================================================

"""
# !usr/bin/python
# -*- coding: UTF-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/7/15
Project ： PyCharm
File  : test_selenium
E-mail: zh13997821732@163.com


================================================================================

"""

import time
from time import sleep
import selenium
import yaml
from selenium import webdriver
import pytest
from selenium.webdriver import TouchActions, ActionChains

from selenium.webdriver.chrome.options import Options
import random


def get_datas():
    # 打开yml文件 这种表示方式防止数据中有中文存在乱码情况
    with open('../datas/information.yml', "r", encoding="utf-8") as f:
        # 读取yml文件中的内容
        data = yaml.safe_load(f)
    return data


class Test_Add_Member:
    # @pytest.mark.skip
    def get_random_email(self):
        email_num = ''
        for i in range(8):
            num = random.randint(0, 9)
            s = str(random.choice([num]))
            email_num += s
        email = email_num + '@163.com'
        return email

    def get_random_number(self):
        num1 = ''
        # 预置12位数的账号
        for i in range(12):
            # 取12个数字并拼接
            num = (random.randint(0, 9))
            s = str(random.choice([num]))
            num1 += s
        return num1

    def get_random_account(self):
        account = ""
        # 生成随机的8位数，8次循环
        for i in range(8):
            # 从0到9 中随便取整数
            num = random.randint(0, 9)
            # num = chr(random.randint(48,57))  # ASCII表示数字
            letter = chr(random.randint(97, 122))  # 取小写字母
            Letter = chr(random.randint(65, 90))  # 取大写字母
            s = str(random.choice([num, letter, Letter]))  # 从三种中随机取数据
            account += s
        accountzh = account + 'zh'
        return accountzh

    def get_department_name(self):
        first_name = ["王", "李", "张", "刘", "赵", "蒋", "孟", "陈", "徐", "杨", "沈", "马", "高", "殷", "上官", "钟", "常"]
        name2 = random.choice(first_name)
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xfe)
        val = f'{head:x} {body:x}'
        str1 = name2 + (bytes.fromhex(val).decode('gb2312')) + '部门'
        return str1

    # @pytest.mark.parametrize("name,account,email1", get_datas()['datas'])
    # def test_remote_chrome(self, name, account, email1):
    def test_remote_chrome(self):
        """
        复用浏览器到添加成员界面
        """
        departmentname = self.get_department_name()  # 部门
        email = self.get_random_email()  # 邮箱
        number = self.get_random_number()  # 账号
        accountzh = self.get_random_account()  # 姓名

        # 实例化 options
        option = Options()
        # 设定chrome debug 模式的一个地址
        # 设置opption的启动地址为127.0.0.1.9222
        option.debugger_address = "127.0.0.1:9222"
        # 实例化一个driver，driver 中设定了刚刚的debuggeraddress属性
        driver = webdriver.Chrome(options=option)
        driver.implicitly_wait(30)
        # 获取添加成员的url
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        time.sleep(3)
        # 点击通讯录
        driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
        #找第一页所有的包含邮箱的元素
        element = driver.find_elements_by_xpath(
            '//*[@id="member_list"]//td[@class="member_colRight_memberTable_td member_colRight_memberTable_td_col5"]')
        a=[]
        for i in element :
            b = i.get_attribute('title')
            a.append(b)
        print(a)
        result = str(a)
        result1 = '68025880@163.com'
        result_final = result1 in result
        if result_final:
            print('添加成功！！！')
        else:
            print('添加失败咯！！！')
            # if str(b) == '68025880@163.com':
            #     print('添加成功')
            #     break
            # else:
            #     pass



