#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

from selenium import webdriver


def deleteAllCourse():
    driver = webdriver.Chrome(r"D:\安装包\chromedriver_win32\chromedriver.exe")
    driver.get("http://localhost/mgr/login/login.html")
    driver.implicitly_wait(5)
    driver.find_element_by_id("username").send_keys("auto")
    driver.find_element_by_id("password").send_keys("sdfsdfsdf")
    driver.find_element_by_css_selector(".btn-success").click()
    time.sleep(3)
    while True:
        btns = driver.find_elements_by_tag_name("button")
        if len(btns) >= 4:
            btns[3].click()
            time.sleep(1)
            driver.find_element_by_css_selector(".btn-primary").click()
            time.sleep(3)
        else:
            break
    driver.quit()
