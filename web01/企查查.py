
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get("https://www.qcc.com/")
driver.maximize_window()
# 鼠标悬停
ac = ActionChains(driver)
ss=driver.find_element_by_link_text("登录 | 注册")
ac.move_to_element(ss).perform() # perform 执行
time.sleep(3)

ss.click()
time.sleep(2)
# 滑动操作
ele=driver.find_element_by_id("nc_1_n1z")
# ele = driver.find_element_by_xpath("//span[@class='nc_iconfont btn_slide']")
# ele = driver.find_element_by_class_name("nc-lang-cnt")
ac.click_and_hold(ele).move_by_offset(348,0).perform()
time.sleep(2)
driver.quit()


