#!/usr/bin/python
#-*-coding:utf-8-*-
from appium import webdriver
import pytest
import yaml
from time import sleep
@pytest.fixture()
def lian():
    d = {
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "emulator-5554",
        "appPackage": "com.facishare.fs",
        "appActivity": ".account_system.ShowNewGuideMapActivity",
        "noReset": "true"
    }
    dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=d)
    sleep(3)
    return dr

@pytest.fixture()
def xi():
    with open(file=r'D:\PyCharm1903\FXXK\element\1.yaml',mode='r',encoding='utf-8') as f:
        e=yaml.load(f,Loader=yaml.FullLoader)
    return e