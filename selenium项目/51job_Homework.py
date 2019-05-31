#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

from selenium import webdriver

driver = webdriver.Chrome(r"D:\安装包\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.51job.com/")

driver.find_element_by_id("kwdselectid").send_keys("python")

driver.find_element_by_id("work_position_input").click()
clicked_items = driver.find_elements_by_css_selector("#work_position_click_center_right_list_000000 em.on")
print(clicked_items)
time.sleep(3)
for item in clicked_items:
    print(item.text)
    item.click()

time.sleep(10)
item = driver.find_element_by_css_selector(
    "#work_position_click_center_right_list_000000  #work_position_click_center_right_list_category_000000_080200")
print(item.text)
time.sleep(10)
item.click()

# driver.find_element_by_class_name("work_position_click_close").click()
#
# driver.find_element_by_css_selector(".ush.top_wrap button").click()
#
# jobs=driver.find_elements_by_css_selector("#resultList .el")
# for job in jobs[1:]:
#     job_name=job.find_element_by_css_selector(".t1 a").text
#     company_name=job.find_element_by_css_selector(".t2 a").text
#     job_city=job.find_element_by_class_name("t3").text
#     job_salary=job.find_element_by_class_name("t4").text
#     job_time=job.find_element_by_class_name("t5").text
#     print(job_name,job_city,job_salary,job_time)

driver.quit()
