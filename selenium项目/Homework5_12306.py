#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

from selenium import webdriver

driver = webdriver.Chrome(r"D:\安装包\chromedriver_win32\chromedriver.exe")
driver.get(" https://kyfw.12306.cn/otn/leftTicket/init")
driver.implicitly_wait(10)

# 输入始发站
start = driver.find_element_by_id("fromStationText")
start.click()
start.send_keys("南京南\n")

# 输入目的地
end = driver.find_element_by_id("toStationText")
end.click()
end.send_keys("杭州东\n")

# 选择发车时间
driver.find_element_by_id("cc_start_time").click()
driver.find_element_by_xpath("//option[@value='06001200']").click()  # 选择6:00-12:00

# 选择当前日期的下一天
driver.find_element_by_xpath("//div[@id='date_range']//li[2]").click()

# 点击查询
# driver.find_element_by_id("query_ticket").click()
# time.sleep(3)


trs = driver.find_elements_by_xpath("//*[@id='queryLeftTable']//tr")  # 查找所有的行
time.sleep(3)

for tr in trs:
    if tr.get_attribute("style") == 'display: none;':  # 删除不显示的行
        trs.remove(tr)

for tr in trs:
    sencod_sit = tr.find_element_by_xpath("./td[4]")  # 获取二等座的元素
    if (sencod_sit.text != "无" and sencod_sit.text != "--"):  # 判断二等座是否有座
        train = tr.find_element_by_xpath(".//td[1]//a[1]")  # 获取车次
        print(train.text)

driver.quit()
