#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from selenium import webdriver

driver = webdriver.Chrome(r"D:\安装包\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("http://music.163.com/#/discover/toplist?id=60198")

driver.switch_to_frame("contentFrame")  # 切换到iframe
ele = driver.find_element_by_id('song-list-pre-cache')
print(ele.text)

driver.switch_to_default_content()  # 切换回来
ele = driver.find_element_by_id("g_nav2")
print(ele.text)
driver.quit()
