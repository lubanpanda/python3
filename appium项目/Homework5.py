#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

from appium import webdriver

try:
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "7.1",
        "deviceName": "test",
        "appPackage": "io.manong.developerdaily",
        "appActivity": "io.toutiao.android.ui.activity.LaunchActivity",
        "noReset": True,
        "newCommandTimeout": 6000,
        "sessionOverride": True
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    driver.implicitly_wait(10)

    # 点击第一篇文章，判断点进去的是否为同一篇
    first_artical = driver.find_element_by_xpath(  # 第一篇文章元素
        "//*[@resource-id='io.manong.developerdaily:id/btn_item']//*[@class='android.widget.RelativeLayout']/*[@resource-id='io.manong.developerdaily:id/tv_title']")
    title = first_artical.text  # 获取标题文本
    first_artical.click()  # 点击进入文章
    ele_title = driver.find_element_by_xpath(
        "//*[@resource-id='io.manong.developerdaily:id/header_view']/*[@resource-id='io.manong.developerdaily:id/tv_title']").text
    print(title)
    print(ele_title)
    if (title == ele_title):
        print("能打开同一篇文章")
    else:
        print("不能打开同一篇文章")
    driver.press_keycode(4)  # 返回

    time.sleep(3)
    # 判断能够正确返回 阅读标签页
    read_ele = driver.find_elements_by_xpath("//*[@resource-id='io.manong.developerdaily:id/viewPager']")
    if read_ele:
        print("返回阅读标签页")
    else:
        print("未返回阅读标签")
except:
    print("错误")

driver.quit()
