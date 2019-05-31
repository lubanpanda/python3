#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from selenium import webdriver

driver = webdriver.Chrome(r"D:\安装包\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("http://music.baidu.com/top/new")

eles = driver.find_elements_by_id("songListWrapper")

driver.quit()
