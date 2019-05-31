#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 作业2
import time

from selenium import webdriver

driver = webdriver.Chrome(r"D:\安装包\chromedriver_win32\chromedriver.exe")
driver.get(" https://tinypng.com/ ")

driver.find_element_by_css_selector(".target .icon").click()
import win32com.client

shell = win32com.client.Dispatch("WScript.shell")
shell.sendkeys(r"D:\tupian.jpg" + "\n")
time.sleep(4)
driver.quit()
