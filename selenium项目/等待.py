#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 隐式等待
from selenium import webdriver

driver = webdriver.Chrome("")
driver.implicitly_wait(10)  # 隐式等待10s

# 显示等待:为一个操作专门指定等待时间
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

ele = WebDriverWait(driver, 60).until(EC.presence_of_element_located(By.ID, 'username'))
