#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
import traceback

from appium import webdriver

try:
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "7.1",
        "deviceName": "test",
        "appPackage": "com.example.jcy.wvtest",
        "appActivity": "com.example.jcy.wvtest.MainActivity",
        "noReset": True,
        "newCommandTimeout": 2000,
        "sessionOverride": True,
        "chromedriverExecutable": r"D:\安装包\chromedriver_win32\62.0\chromedriver.exe"
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    driver.implicitly_wait(10)
    time.sleep(5)

    driver.switch_to.context("WEBVIEW_com.example.jcy.wvtest")
    driver.find_element_by_id("index-kw").send_keys("松勤")
    driver.find_element_by_id("index-bn").click()

    driver.switch_to.context("NATIVE_APP")
    time.sleep(3)
    driver.find_element_by_id("com.example.jcy.wvtest:id/navigation_notifications").click()
except:
    print(traceback.format_exc())
driver.quit()
