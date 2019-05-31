#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(r"D:\安装包\chromedriver_win32\chromedriver.exe")
driver.get("https://www.vmall.com/")

first = driver.current_window_handle
driver.find_element_by_css_selector("[href='http://consumer.huawei.com/cn/']").click()  # 点击华为官网
handles = driver.window_handles
for handle in handles:
    if handle != first:
        second = handle
driver.switch_to.window(second)  # 切换到华为官网

menus = driver.find_elements_by_css_selector(".products-name")  # 获取菜单项
text = ""
for menu in menus:  # 遍历菜单项，获取文本信息
    text = text + menu.text + "|"
print(text)
if text == "智能手机|笔记本|平板|智能穿戴|智能家居|更多产品|软件应用|服务与支持|":
    print("pass")
else:
    print("fail")

driver.switch_to.window(first)  # 切换到华为首页
ActionChains(driver).move_to_element(driver.find_element_by_id("zxnav_1")).perform()  # 鼠标悬停在笔记本&平板
driver.execute_script("setTimeout(function(){debugger},3000)")  # 冻结窗口

pc_menus = driver.find_elements_by_css_selector(".category-panels-1 span")  # 获取右侧菜单列表项
text = ""
for pc_menu in pc_menus[:3]:  # 获取前三位的文本内容（存在隐藏菜单）
    text = text + pc_menu.text + "|"
if text == "平板电脑|笔记本电脑|笔记本配件|":
    print("pass")
else:
    print("fail")

driver.quit()
