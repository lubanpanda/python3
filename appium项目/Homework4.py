#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 找到一个安卓设备（没有可以向朋友借用一下）
# 安装松勤自动化练习APK，点击这里下载安装
# 写自动化测试，实现滚动到口碑最佳部分，并且打印出所有口碑最佳部分的5个应用

import time

from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "platformVersion": "7.1",
    "deviceName": "test",
    # "app":r"D:\sqauto.apk",
    "appPackage": "com.sqauto",
    "appActivity": "com.sqauto.MainActivity",
    "noReset": True,
    "newCommandTimeout": 6000,
    "sessionOverride": True
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)

window = driver.get_window_size()  # 获取窗口长宽
width = window['width']
height = window['height']

for i in range(3):  # 循环滑动三次
    time.sleep(5)
    driver.swipe(start_x=width / 2, start_y=int(height * 0.75), end_x=width / 2, end_y=int(height * 0.1), duration=3000)
eles = driver.find_elements_by_xpath("//*[@content-desc='best reputation']/following-sibling::android.widget.TextView")

# 打印出应用名
i = 0
for ele in eles:
    if i % 2 == 0 and ele.text != "用户最爱":
        print(ele.text)
    if ele.text == "用户最爱":
        break
    i += 1
time.sleep(3)
driver.quit()
