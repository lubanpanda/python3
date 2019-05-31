import time

from selenium import webdriver

driver = webdriver.Chrome(r"D:\安装包\chromedriver_win32\chromedriver.exe")
driver.get("http://www.51job.com")
driver.implicitly_wait(10)

driver.find_element_by_css_selector(".more").click()  # 点击“高级搜索”
driver.find_element_by_id("kwdselectid").send_keys("python")  # 输入关键字“python”
time.sleep(3)
driver.find_element_by_css_selector(".tl .bg").click()

# 地区选择
driver.find_element_by_css_selector(".addbut .dicon").click()  # 点击“+”号
clicked_city = driver.find_elements_by_css_selector("#work_position_click_center_right_list_000000 .on")  # 查找当前被选中的城市
for city in clicked_city:  # 遍历选中的程序，点击取消选中
    time.sleep(3)
    city.click()
    time.sleep(3)
hangzhou = driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200")  # 查找杭州，并点击选中
hangzhou.click()
time.sleep(5)
driver.find_element_by_id("work_position_click_bottom_save").click()  # 点击“确定”按钮

# 职能类别
driver.find_element_by_id("funtype_click").click()  # 点击“+”号
driver.find_element_by_id("funtype_click_center_left_each_0100").click()  # 点击“计算机/互联网/通信/电子/"
driver.find_element_by_css_selector(".js_more em[data-value='0100']").click()  # 点击“计算机软件“
driver.find_element_by_css_selector("em[data-value='0106']").click()  # 点击“高级软件工程师”
driver.find_element_by_id("funtype_click_bottom_save").click()  # 点击“确定”按钮

# 公司性质
driver.find_element_by_css_selector("#cottype_list  .i_arrow").click()  # 点击工作性质
driver.find_element_by_css_selector(".li[title='外资（欧美）']").click()  # 选择“外资（欧美）”

# 工作年限
driver.find_element_by_css_selector("#workyear_list .ic").click()  # 点击工作年限
driver.find_element_by_css_selector(".li[title='1-3年']").click()  # 点击“1-3年”

# 搜索
driver.find_element_by_css_selector(".btnbox .p_but").click()  # 点击搜索

# 获取职位信息
infos = driver.find_elements_by_css_selector("#resultList .el")
for info in infos[1:]:
    job = info.text.split("\n")
    print("%s|%s|%s|%s|%s" % (job[0], job[1], job[2], job[3], job[4]))

driver.quit()
