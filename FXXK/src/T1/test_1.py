#!/usr/bin/python
#-*-coding:utf-8-*-
from appium import webdriver
import pytest
from time import sleep
from until.huadong import *
from time import sleep


#测试介绍界面正常滑动
# def test_1(lian):
#     sleep(5)
#     swipe(lian)

'''
验证app正常登陆
def test_2(lian,xi):
    lian.find_element_by_id(xi['in']).click()
    sleep(2)
    lian.find_element_by_id(xi['send']).clear()
    sleep(2)
    lian.find_element_by_id(xi['send']).send_keys('13014623984')
    sleep(2)
    lian.find_element_by_id(xi['passwd']).send_keys('1234qwer')
    sleep(2)
    lian.find_element_by_id(xi['login']).click()
    sleep(8)
    t = lian.find_element_by_id('com.facishare.fs:id/tabLayout').find_element_by_class_name('android.widget.LinearLayout').find_element_by_class_name('android.widget.TextView').text
    assert t =='企信'
'''

'''
#验证功能模块正常切换
def test_3(lian,xi):
    lian.find_element_by_id(xi['in']).click()
    sleep(2)
    lian.find_element_by_id(xi['send']).clear()
    sleep(2)
    lian.find_element_by_id(xi['send']).send_keys('13014623984')
    sleep(2)
    lian.find_element_by_id(xi['passwd']).send_keys('1234qwer')
    sleep(2)
    lian.find_element_by_id(xi['login']).click()
    sleep(8)
    t1=lian.find_element_by_id(xi['tool']).find_element_by_class_name(xi['tubiao']).find_elements_by_class_name(xi['tubiao'])
    for i in t1:
        i.click()
    sleep(2)
    t2=lian.find_element_by_id('com.facishare.fs:id/tv_coll_name').text
    assert t2=='萤火虫梦'
'''

#验证成功退出账号
def test_4(lian,xi):
    denglu(lian,xi)
    sleep(3)
    up_down(lian)
    sleep(3)
    t3=lian.find_element_by_id(xi['wode']).find_elements_by_id('com.facishare.fs:id/LinearLayout_h_view')
    t3[6].click()
    sleep(3)
    lian.find_element_by_id(xi['exit']).click()
    sleep(2)
    lian.find_element_by_id(xi['en']).click()


