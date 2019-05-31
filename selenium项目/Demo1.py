#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

from selenium import webdriver

driver = webdriver.Chrome(r"D:\安装包\chromedriver_win32\chromedriver.exe")
driver.get("https://www.baidu.com")
element_keyword = driver.find_element_by_id("kw")
element_keyword.send_keys("松勤")
element_button = driver.find_element_by_id("su")
element_button.click()
time.sleep(2)
element_text = driver.find_element_by_id("1")
print(element_text.text)
driver.quit()
