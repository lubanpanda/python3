#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "platformVersion": "7.1",
    "deviceName": "test",
    "app": r"D:\duoduo.apk",
    "appPackage": "com.ibox.calculators",  # app包名
    "appActivity": "com.ibox.calculators.SplashActivity",
    # 'unicodeKeyboard':True,#指定输入法
    "noReset": True,
    "newCommandTimeout": 6000,
}
# 启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

time.sleep(5)
driver.find_element_by_id("digit3").click()
driver.find_element_by_id("plus").click()
driver.find_element_by_id("digit9").click()
driver.find_element_by_id("equal").click()
driver.find_element_by_id("mul").click()
driver.find_element_by_id("digit5").click()
driver.find_element_by_id("equal").click()

answer = driver.find_element_by_xpath("//*[@resource-id='com.ibox.calculators:id/cv']//android.widget.TextView[2]").text
print(answer)
if (answer == '60'):
    print("测试通过")
else:
    print("测试不通过")
