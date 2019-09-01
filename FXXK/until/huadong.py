#!/usr/bin/python
#-*-coding:utf-8-*-
from appium import webdriver
from time import sleep
def swipe(drive,t=500):
    l = drive.get_window_size()
    x1 = l['width'] * 0.7
    x2 = l['width'] * 0.4
    y1 = l['height'] * 0.5
    for i in range(1,4):
        drive.swipe(x1,y1,x2,y1,duration=t)
        sleep(2)
    for j in range(1,4):
        drive.swipe(x2,y1,x1,y1,duration=t)
        sleep(2)

def up_down(dr,t=500):
    l1= dr.get_window_size()
    x1 = l1['width'] * 0.5
    x2 = l1['width'] * 0.5
    y1 = l1['height'] * 0.7
    y2 = l1['height'] * 0.3
    dr.swipe(x1,y1,x2,y2,duration=t)


def denglu(dd,xi):
    dd.find_element_by_id(xi['in']).click()
    sleep(2)
    dd.find_element_by_id(xi['send']).clear()
    sleep(2)
    dd.find_element_by_id(xi['send']).send_keys('13014623984')
    sleep(2)
    dd.find_element_by_id(xi['passwd']).send_keys('1234qwer')
    sleep(2)
    dd.find_element_by_id(xi['login']).click()
    sleep(8)
    t1=dd.find_element_by_id(xi['tool']).find_element_by_class_name(xi['tubiao']).find_elements_by_class_name(xi['tubiao'])
    for i in t1:
        i.click()
    sleep(2)




